/*
 * $LastChangedRevision: 853 $
 * $LastChangedDate:: 2015-11-26 15:56:03 +0100#$
 *
 * Copyright (c) 2015 Linz Center of Mechatronics GmbH
 * All rights reserved.
 */
#include "CircularByteBuffer.h"
#include "CommunicationCDC.h"

typedef enum
{
    /* Application's state machine's initial state. */
    COM_STATE_INIT=0,

    /* Application waits for device configuration*/
    COM_STATE_WAIT_FOR_CONFIGURATION,

    /* Wait for a character receive */
    COM_STATE_SCHEDULE_READ,

    /* A character is received from host */
    COM_STATE_WAIT_FOR_READ_COMPLETE,

    /* Wait for the TX to get completed */
    COM_STATE_SCHEDULE_WRITE,

    /* Wait for the write to complete */
    COM_STATE_WAIT_FOR_WRITE_COMPLETE,

    /* Application Error state*/
    COM_STATE_ERROR

} VIRTUAL_COM_STATE;

typedef struct {
	void (*send)(tInterface*, uint8);               /** Function link to send character */
	uint8 (*receive)(tInterface*);                  /** Function link to receive character */
	uint8 (*isReceiveDataAvailable)(tInterface*);   /** Function link to check if receive data is available */
	uint8 (*isSendReady)(tInterface*);              /** Function link to check if data can be sent */
	uint8 (*getTxFifoFree)(tInterface*);            /** Function link to check if transmit FIFO is ready to be filled */
	void (*flush)(tInterface*);                     /** Function link to flush data */
    
    /* Device layer handle returned by device layer open function */
    USB_DEVICE_HANDLE deviceHandle;

    /* Application's current state*/
    VIRTUAL_COM_STATE state;

    /* Set Line Coding Data */
    USB_CDC_LINE_CODING setLineCodingData;

    /* Device configured state */
    bool isConfigured;

    /* Get Line Coding Data */
    USB_CDC_LINE_CODING getLineCodingData;

    /* Control Line State */
    USB_CDC_CONTROL_LINE_STATE controlLineStateData;

    /* Read transfer handle */
    USB_DEVICE_CDC_TRANSFER_HANDLE readTransferHandle;

    /* Write transfer handle */
    USB_DEVICE_CDC_TRANSFER_HANDLE writeTransferHandle;

    /* True if a character was read */
    bool isReadComplete;

    /* True if a character was written*/
    bool isWriteComplete;

    /* Flag determines SOF event occurrence */
    bool sofEventHasOccurred;

    /* Break data */
    uint16_t breakData;

    /* Switch debounce timer */
    unsigned int switchDebounceTimer;

    unsigned int debounceCount;
} tVirtualSerial;

static tVirtualSerial globalSerial;

#ifndef CDC_READBUFFER_SIZE
#define CDC_READBUFFER_SIZE (512)
#endif

static uint8 __attribute__((coherent)) __attribute__((aligned(4))) cdcReadBuffer[CDC_READBUFFER_SIZE];
static uint8 __attribute__((coherent)) __attribute__((aligned(4))) cdcWriteBuffer[1];

#ifndef USER_RX_DATABUFFER_SIZE
#define USER_RX_DATABUFFER_SIZE (256)
#endif
static uint8 circularDataBuffer[USER_RX_DATABUFFER_SIZE];
static tCircularByteBuffer rxBuffer;

/* private prototypes */
static void sendByte(tVirtualSerial* vSerial, uint8 data);
static uint8 readByte(tVirtualSerial* vSerial);
static uint8 isReadyToSend(tVirtualSerial* vSerial);
static uint8 isDataAvailable(tVirtualSerial* vSerial);
static void flush(tVirtualSerial* vSerial);
static uint8 getTxFifoFree(tVirtualSerial* vSerial);

static void USBDeviceEventHandler(USB_DEVICE_EVENT event, void* eventData, uintptr_t context);
static bool checkReset(tVirtualSerial* vSerial);

void initCommunication(void)
{
    /* Place the App state machine in its initial state. */
    globalSerial.state = COM_STATE_INIT;
    
    /* Device Layer Handle  */
    globalSerial.deviceHandle = USB_DEVICE_HANDLE_INVALID ;

    /* Device configured status */
    globalSerial.isConfigured = false;

	globalSerial.getLineCodingData.dwDTERate = 115200;
    globalSerial.getLineCodingData.bParityType = 0;
    globalSerial.getLineCodingData.bCharFormat = 1;
    globalSerial.getLineCodingData.bDataBits = 8;

    /* Read Transfer Handle */
    globalSerial.readTransferHandle = USB_DEVICE_CDC_TRANSFER_HANDLE_INVALID;

    /* Write Transfer Handle */
    globalSerial.writeTransferHandle = USB_DEVICE_CDC_TRANSFER_HANDLE_INVALID;

    /* Intialize the read complete flag */
    globalSerial.isReadComplete = true;

    /*Initialize the write complete flag*/
    globalSerial.isWriteComplete = true;

    /* Reset the switch debounce counter */
    globalSerial.switchDebounceTimer = 0;

    /* Reset other flags */
    globalSerial.sofEventHasOccurred = false;
    
    /* function pointers */
    globalSerial.send = (void (*)(tInterface*, uint8))sendByte;
    globalSerial.receive = (uint8 (*)(tInterface*))readByte;
    globalSerial.isReceiveDataAvailable = (uint8 (*)(tInterface*))isDataAvailable;
    globalSerial.isSendReady = (uint8 (*)(tInterface*))isReadyToSend;
    globalSerial.flush = (void (*)(tInterface*))flush;
    globalSerial.getTxFifoFree = (uint8 (*)(tInterface*))getTxFifoFree;
    
    initBuffer(&rxBuffer, circularDataBuffer, USER_RX_DATABUFFER_SIZE);
}

/**
 * Initializes USB device layer and returns success state.
 * @return Initialization success state
 */
uint8 initCommunicationHardware(void)
{
    uint8 success;
    
    globalSerial.deviceHandle = USB_DEVICE_Open(USB_DEVICE_INDEX_0, DRV_IO_INTENT_READWRITE);
    if (globalSerial.deviceHandle != USB_DEVICE_HANDLE_INVALID)
    {
        success = (uint8)1;
        USB_DEVICE_EventHandlerSet(globalSerial.deviceHandle, USBDeviceEventHandler, 0);
    }
    else
    {
        success = (uint8)0;
    }
    return (success);
}

/**
 * Returns USB configuration state.
 * 
 * @return Configuration state
 */
uint8 isCommunicationConfigured(void)
{
    uint8 success;
    if (globalSerial.isConfigured)
    {
        success = (uint8)1;
    }
    else
    {
        success = (uint8)0;
    }
    return (success);
}

void linkCommunication(tProtocol* protocol)
{
    protocol->hwInterface = (tInterface*)&globalSerial;
}

static void sendByte(tVirtualSerial* vSerial, uint8 data)
{
    cdcWriteBuffer[0] = data;

    vSerial->writeTransferHandle = USB_DEVICE_CDC_TRANSFER_HANDLE_INVALID;
    vSerial->isWriteComplete = false;
    USB_DEVICE_CDC_Write(USB_DEVICE_CDC_INDEX_0, &vSerial->writeTransferHandle, \
            cdcWriteBuffer, 1, USB_DEVICE_CDC_TRANSFER_FLAGS_DATA_COMPLETE);
}


static uint8 readByte(tVirtualSerial* vSerial)
{
    uint8 data;
    readData(&rxBuffer, &data);  
    return (data);
}

static uint8 isReadyToSend(tVirtualSerial* vSerial)
{
    uint8 readyToSend;
    
    checkReset(vSerial);
    
    if (vSerial->isConfigured && vSerial->isWriteComplete)
    {
        readyToSend = (uint8)1;
    }
    else
    {
        readyToSend = (uint8)0;
    }
    return (readyToSend);
}

static uint8 isDataAvailable(tVirtualSerial* vSerial)
{
    uint8 dataAvailable;
    if (getUsedBytes(&rxBuffer) > 0)
    {
        dataAvailable = (uint8)1;
    }
    else
    {
        dataAvailable = (uint8)0;
    }
    
    checkReset(vSerial);
    
    if (vSerial->isConfigured && vSerial->isReadComplete)
    {
        vSerial->isReadComplete = false;
        USB_DEVICE_CDC_Read (USB_DEVICE_CDC_INDEX_0, &vSerial->readTransferHandle, cdcReadBuffer, CDC_READBUFFER_SIZE);
        if(vSerial->readTransferHandle == USB_DEVICE_CDC_TRANSFER_HANDLE_INVALID)
        {
            vSerial->state = COM_STATE_ERROR;
        }
    }

    return (dataAvailable);
}

static void flush(tVirtualSerial* vSerial)
{
    ;
}

static uint8 getTxFifoFree(tVirtualSerial* vSerial)
{
    return ((uint8)0);
}


/**
 * USB CDC device application event handler.
 * @param index Index
 * @param event Event
 * @param pData Event data
 * @param userData User data
 * @return Event response
 */
USB_DEVICE_CDC_EVENT_RESPONSE USBDeviceCDCEventHandler(USB_DEVICE_CDC_INDEX index, USB_DEVICE_CDC_EVENT event, \
        void* pData, uintptr_t userData)
{
    tVirtualSerial* vSerial = (tVirtualSerial*)userData;
    USB_CDC_CONTROL_LINE_STATE* controlLineStateData;

    switch (event)
    {
        case USB_DEVICE_CDC_EVENT_GET_LINE_CODING:
            /* This means the host wants to know the current line
             * coding. This is a control transfer request. Use the
             * USB_DEVICE_ControlSend() function to send the data to
             * host.  */
            USB_DEVICE_ControlSend(vSerial->deviceHandle,
                    &vSerial->getLineCodingData, sizeof(USB_CDC_LINE_CODING));
            break;
        case USB_DEVICE_CDC_EVENT_SET_LINE_CODING:
            /* This means the host wants to set the line coding.
             * This is a control transfer request. Use the
             * USB_DEVICE_ControlReceive() function to receive the
             * data from the host */
            USB_DEVICE_ControlReceive(vSerial->deviceHandle,
                    &vSerial->setLineCodingData, sizeof(USB_CDC_LINE_CODING));
            break;
        case USB_DEVICE_CDC_EVENT_SET_CONTROL_LINE_STATE:
            /* This means the host is setting the control line state.
             * Read the control line state. We will accept this request
             * for now. */
            controlLineStateData = (USB_CDC_CONTROL_LINE_STATE *)pData;
            vSerial->controlLineStateData.dtr = controlLineStateData->dtr;
            vSerial->controlLineStateData.carrier = controlLineStateData->carrier;
            USB_DEVICE_ControlStatus(vSerial->deviceHandle, USB_DEVICE_CONTROL_STATUS_OK);
            break;
        case USB_DEVICE_CDC_EVENT_SEND_BREAK:
            /* This means that the host is requesting that a break of the
             * specified duration be sent. Read the break duration */
            vSerial->breakData = ((USB_DEVICE_CDC_EVENT_DATA_SEND_BREAK *)pData)->breakDuration;
            break;
        case USB_DEVICE_CDC_EVENT_READ_COMPLETE:
        {
            /* This means that the host has sent some data*/
            uint16 rxLen = (uint16)((USB_DEVICE_CDC_EVENT_DATA_READ_COMPLETE*)pData)->length;
            putData(&rxBuffer, cdcReadBuffer, rxLen);
            vSerial->isReadComplete = true;
            break;
        }
        case USB_DEVICE_CDC_EVENT_CONTROL_TRANSFER_DATA_RECEIVED:
            /* The data stage of the last control transfer is
             * complete. For now we accept all the data */
            USB_DEVICE_ControlStatus(vSerial->deviceHandle, USB_DEVICE_CONTROL_STATUS_OK);
            break;
        case USB_DEVICE_CDC_EVENT_CONTROL_TRANSFER_DATA_SENT:
            /* This means the GET LINE CODING function data is valid. We dont
             * do much with this data in this demo. */
            break;
        case USB_DEVICE_CDC_EVENT_WRITE_COMPLETE:
            /* This means that the data write got completed. We can schedule
             * the next read. */
            vSerial->isWriteComplete = true;
            break;
        default:
            break;
    }

    return USB_DEVICE_CDC_EVENT_RESPONSE_NONE;
}

/**
 * Application USB device layer event handler.
 * @param event Event
 * @param eventData Event data
 * @param context Context
 */
static void USBDeviceEventHandler (USB_DEVICE_EVENT event, void* eventData, uintptr_t context)
{
    USB_DEVICE_EVENT_DATA_CONFIGURED *configuredEventData;

    switch (event)
    {
        case USB_DEVICE_EVENT_SOF:
            /* This event is used for switch debounce. This flag is reset
             * by the switch process routine. */
            globalSerial.sofEventHasOccurred = true;
            break;
        case USB_DEVICE_EVENT_RESET:
            globalSerial.isConfigured = false;
            break;
        case USB_DEVICE_EVENT_CONFIGURED:
            /* Check the configuratio. We only support configuration 1 */
            configuredEventData = (USB_DEVICE_EVENT_DATA_CONFIGURED*)eventData;
            if (configuredEventData->configurationValue == 1)
            {
                /* Register the CDC Device application event handler here.
                 * Note how the appData object pointer is passed as the
                 * user data */
                USB_DEVICE_CDC_EventHandlerSet(USB_DEVICE_CDC_INDEX_0, USBDeviceCDCEventHandler, (uintptr_t)&globalSerial);

                /* Mark that the device is now configured */
                globalSerial.isConfigured = true;
            }
            break;
        case USB_DEVICE_EVENT_POWER_DETECTED:
            /* VBUS was detected. We can attach the device */
            USB_DEVICE_Attach(globalSerial.deviceHandle);
            break;
        case USB_DEVICE_EVENT_POWER_REMOVED:
            /* VBUS is not available any more. Detach the device. */
            USB_DEVICE_Detach(globalSerial.deviceHandle);
            break;
        case USB_DEVICE_EVENT_SUSPENDED:
            break;
        case USB_DEVICE_EVENT_RESUMED:
        case USB_DEVICE_EVENT_ERROR:
        default:
            break;
    }
}

/**
 * Checks and returns reset state.
 * @param vSerial Virtual serial interface
 * @return  Reset state
 */
static bool checkReset(tVirtualSerial* vSerial)
{
    /* This function returns true if the device was reset  */
    bool isReset;

    if(vSerial->isConfigured == false)
    {
        vSerial->state = COM_STATE_WAIT_FOR_CONFIGURATION;
        vSerial->readTransferHandle = USB_DEVICE_CDC_TRANSFER_HANDLE_INVALID;
        vSerial->writeTransferHandle = USB_DEVICE_CDC_TRANSFER_HANDLE_INVALID;
        vSerial->isReadComplete = true;
        vSerial->isWriteComplete = true;
        isReset = true;
    }
    else
    {
        isReset = false;
    }

    return(isReset);
}
