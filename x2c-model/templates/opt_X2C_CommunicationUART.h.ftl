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
 
 /** @file
 * @brief Virtual serial interface via USB.
 * 
 * Virtual serial interface uses CDC via USB for serial communication.
 * 
 * @warning Currently only one interface is supported due to the need of static-global variables.
 * @warning Driver does not allow to pass a userdata pointer to all callback functions.
 */
 
#ifndef __COMMUNICATIONX2C_H__
#define __COMMUNICATIONX2C_H__

// ChB #include "system_config.h"
// ChB #include "system_definitions.h"
#include "CommonFcts.h"
#include "Target.h"

typedef struct {
	void (*send)(tInterface*, uint8);               /** Function link to send character */
	uint8 (*receive)(tInterface*);                  /** Function link to receive character */
	uint8 (*isReceiveDataAvailable)(tInterface*);   /** Function link to check if receive data is available */
	uint8 (*isSendReady)(tInterface*);              /** Function link to check if data can be sent */
	uint8 (*getTxFifoFree)(tInterface*);            /** Function link to check if transmit FIFO is ready to be filled */
	void (*flush)(tInterface*);                     /** Function link to flush data */
} tSerial;

/* public prototypes */
void initCommunication(tSerial* serial);
void linkCommunication(tProtocol* protocol, tSerial* serial);

#endif
