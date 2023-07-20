/*
 * Copyright (c) 2013, Linz Center of Mechatronics GmbH (LCM)
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification, are permitted
 * provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice, this list of
 * conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright notice, this list of
 * conditions and the following disclaimer in the documentation and/or other materials provided
 * with the distribution.
 *
 * 3. Neither the name of the [organization] nor the names of its contributors may be used to
 * endorse or promote products derived from this software without specific prior written
 * permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
 * AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
 * OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */
#include "device.h"
#include "X2C_Communication.h"
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
