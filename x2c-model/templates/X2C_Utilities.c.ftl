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

// ChB #include "system_definitions.h"
#include "Target.h"
#include "TableStruct.h"
#include "LNet.h"
#include "Services.h"
#include "BlockServices.h"
#include "X2C.h"
#include "X2C_InterfaceHandling.h"
#include "X2C_Communication.h"
#include "X2C_Utilities.h"

<#if X2C_MODEL_COMM_INT == "USB-CDC">
/* Communication state machine */
typedef enum { COMM_PREINIT, COMM_HWINIT, COMM_CONFIGURED, COMM_RUN } tCommStateX2C;
static tCommStateX2C commState = COMM_PREINIT;
</#if>

/* used by init version info */
const struct {
	uint8 date[11];
	uint8 time[8];
} compilationDate = { __DATE__, __TIME__ };

/* X2C maintenance structure */
volatile tTableStruct TheTableStruct;
volatile tTableStruct *TableStruct = &TheTableStruct;

/* LNet protocol buffersize & node identifier */
#define LNET_BUFFERSIZE ((uint8)255)
#define LNET_NODEID ((uint8)1)
#define KICK_DOG \
    do { \
        ClrWdt(); \
    } while (0)

<#if X2C_MODEL_COMM_INT == "UART">
static tSerial interface;
</#if>
static tLNet protocol;
static uint8 bufferLNet[LNET_BUFFERSIZE];

/* private prototypes */
static void initVersionInfo(volatile tTableStruct* tblStruct, uint16 appVersion);


/** 
 * @brief Main function.
 * 
 * @return The main function will never return due to the never ending loop.
 */
void X2C_Initialize(void)
{
    /** - initialize "integrated monitor":
     *    - configuration of LNet protocol:
     *      - Node-ID: 1
     *      - Buffer size: 255
     *      .
     *    .
     *  - initialize serial interface
     */
    initTableStruct();
<#if X2C_MODEL_COMM_INT == "UART">
	initCommunication(&interface);
</#if>
<#if X2C_MODEL_COMM_INT == "USB-CDC">
	initCommunication();
</#if>
    initLNet(&protocol, bufferLNet, LNET_BUFFERSIZE, LNET_NODEID);
<#if X2C_MODEL_COMM_INT == "UART">
	linkCommunication((tProtocol*)&protocol, &interface);
</#if>
<#if X2C_MODEL_COMM_INT == "USB-CDC">
	linkCommunication((tProtocol*)&protocol);
</#if>
    initServiceTable((tProtocol*)&protocol);
    addCoreServices((tProtocol*)&protocol);
    addBlockServices((tProtocol*)&protocol);
    addTableStructProtocol((tProtocol*)&protocol);
    TableStruct->DSPState = PRG_LOADED_STATE;

    initVersionInfo(TableStruct, (uint16)0x0001);   /* software version 1 */
    TableStruct->TFncTable = blockFunctionTable;
    TableStruct->TParamTable = parameterIdTable;

    /** - initialize X2C */
    X2C_Init();
<#if X2C_MODEL_COMM_INT == "USB-CDC">
	commState = COMM_HWINIT;
</#if>
}

void X2C_Communicate(void)
{
<#if X2C_MODEL_COMM_INT == "USB-CDC">
    switch (commState)
    {
        case COMM_HWINIT:
            if (initCommunicationHardware())
            {
                commState = COMM_CONFIGURED;
            }
            break;
        case COMM_CONFIGURED:
            if (isCommunicationConfigured())
            {
                commState = COMM_RUN;
            }
            break;
        case COMM_RUN:
            protocol.communicate((tProtocol*)&protocol);
            break;
        default:
            break;
    }
</#if>
<#if X2C_MODEL_COMM_INT == "UART">
	protocol.communicate((tProtocol*)&protocol);
</#if>
}

void X2C_UpdateModel(void)
{
	readInports();
	X2C_Update();
	writeOutports();
}

/**
 * @brief Routine to set version.
 * 
 * @param tblStruct X2C maintenance structure.
 * @param appVersion Version number.
 */
static void initVersionInfo(volatile tTableStruct* tblStruct, uint16 appVersion)
{
	tblStruct->framePrgVersion = appVersion;
	tblStruct->framePrgCompDateTime = (uint8*)&compilationDate;
}
