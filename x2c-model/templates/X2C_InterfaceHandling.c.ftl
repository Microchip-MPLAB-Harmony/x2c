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

#include "X2C.h"
#include "X2C_InterfaceHandling.h"
#include "definitions.h"

void X2C_ReadInports(void)
{
	/* TODO add linkage hardware-inputs -> X2C inports here 
     * Pass the peripheral values to model Inports
     * if (PORTA & 1) { 
     *    x2cModel.inports.bInport = INT16_MAX;
     * }else {
     *    x2cModel.inports.bInport = 0;
     * }
	 */
	;
}

void X2C_WriteOutports(void)
{
	/* TODO add linkage X2C outports -> hardware-outputs here 
     * if (*x2cModel.outports.bOutport) {  // if model Outport differ than zero 
     *    LATB |= 1; // set LATB0 
     * } else {
     *    LATB &= ~1; // clear LATB0
     * } 
	*/
	;
}
