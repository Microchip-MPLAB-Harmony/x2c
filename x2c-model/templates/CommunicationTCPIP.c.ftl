/*
 * $LastChangedRevision: 853 $
 * $LastChangedDate:: 2015-11-26 15:56:03 +0100#$
 *
 * Copyright (c) 2015 Linz Center of Mechatronics GmbH
 * All rights reserved.
 */
#include "device.h"
#include "CommunicationUART.h"
#include "../tcp_server.h"

//#include "config/default/peripheral/usart/plib_usart1.h"

/* private prototypes */
static void sendByte(tSerial* serial, uint8 data);
static uint8 readByte(tSerial* serial);
static uint8 isReadyToSend(tSerial* serial);
static uint8 isDataAvailable(tSerial* serial);
static void flush(tSerial* serial);
static uint8 getTxFifoFree(tSerial* serial);

void initCommunication(tSerial* serial) {
    /* function pointers */
    serial->send = (void (*)(tInterface*, uint8))sendByte;
    serial->receive = (uint8(*)(tInterface*))readByte;
    serial->isReceiveDataAvailable = (uint8(*)(tInterface*))isDataAvailable;
    serial->isSendReady = (uint8(*)(tInterface*))isReadyToSend;
    serial->flush = (void (*)(tInterface*))flush;
    serial->getTxFifoFree = (uint8(*)(tInterface*))getTxFifoFree;
}

void linkCommunication(tProtocol* protocol, tSerial* serial) {
    protocol->hwInterface = (tInterface*) serial;
}

static void sendByte(tSerial* serial, uint8 data) {
    SendTCPByte(&data);
}

static uint8 readByte(tSerial* serial) {
    return ReadTCPByte();
}

static uint8 isReadyToSend(tSerial* serial) {
    return isTCPReadyToSend();
}

static uint8 isDataAvailable(tSerial* serial) {
    return (isTCPDataAvailable());
}

static void flush(tSerial* serial) {
    ;
}

static uint8 getTxFifoFree(tSerial* serial) {
    return ((uint8) 0);
}
