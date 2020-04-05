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

#include "system_config.h"
#include "system_definitions.h"
#include "CommonFcts.h"
#include "Target.h"

/* public prototypes */
void initCommunication(void);
uint8 initCommunicationHardware(void);
uint8 isCommunicationConfigured(void);

#endif
