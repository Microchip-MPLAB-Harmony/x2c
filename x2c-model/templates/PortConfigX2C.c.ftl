/* This file is part of X2C. http://www.mechatronic-simulation.org/                                                   */

#include "X2C.h"
#include "PortConfigX2C.h"
#include "definitions.h"

void readInports(void)
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

void writeOutports(void)
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
