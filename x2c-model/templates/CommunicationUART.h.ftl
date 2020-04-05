/** @file
 * @brief Virtual serial interface via USB.
 * 
 * Virtual serial interface uses CDC via USB for serial communication.
 * 
 * @warning Currently only one interface is supported due to the need of static-global variables.
 * @warning Driver does not allow to pass a userdata pointer to all callback functions.
 */
/*
 * $LastChangedRevision: 853 $
 * $LastChangedDate:: 2015-11-26 15:56:03 +0100#$
 *
 * Copyright (c) 2015 Linz Center of Mechatronics GmbH
 * All rights reserved.
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
