/*
 * $LastChangedRevision: 853 $
 * $LastChangedDate:: 2015-11-26 15:56:03 +0100#$
 *
 * Copyright (c) 2015 Linz Center of Mechatronics GmbH
 * All rights reserved.
 */
 #include "device.h"
#include "CommunicationUART.h"
#include "definitions.h"

/* private prototypes */
static void sendByte(tSerial* serial, uint8 data);
static uint8 readByte(tSerial* serial);
static uint8 isReadyToSend(tSerial* serial);
static uint8 isDataAvailable(tSerial* serial);
static void flush(tSerial* serial);
static uint8 getTxFifoFree(tSerial* serial);

void initCommunication(tSerial* serial)
{
    /* function pointers */
    serial->send = (void (*)(tInterface*, uint8))sendByte;
    serial->receive = (uint8 (*)(tInterface*))readByte;
    serial->isReceiveDataAvailable = (uint8 (*)(tInterface*))isDataAvailable;
    serial->isSendReady = (uint8 (*)(tInterface*))isReadyToSend;
    serial->flush = (void (*)(tInterface*))flush;
    serial->getTxFifoFree = (uint8 (*)(tInterface*))getTxFifoFree;
}

void linkCommunication(tProtocol* protocol, tSerial* serial)
{
    protocol->hwInterface = (tInterface*)serial;
}

static void sendByte(tSerial* serial, uint8 data)
{
	${X2C_MODEL_PERIPH_USED}_Write( &data, 1 );  // ChB
}

static uint8 readByte(tSerial* serial)
{
	uint8 data;
    bool status = false;
    if(${X2C_MODEL_PERIPH_USED}_ReceiverIsReady())
    {
        status = ${X2C_MODEL_PERIPH_USED}_Read(&data, 1);
        if(status == true)
        {
          return data;  
        }
    }
    return (uint8)(0);
}

static uint8 isReadyToSend(tSerial* serial)
{
	return (${X2C_MODEL_PERIPH_USED}_TransmitterIsReady());
}

static uint8 isDataAvailable(tSerial* serial)
{
	return (${X2C_MODEL_PERIPH_USED}_ReceiverIsReady());  
}

static void flush(tSerial* serial)
{
    ;
}

static uint8 getTxFifoFree(tSerial* serial)
{
    return ((uint8)0);
}
