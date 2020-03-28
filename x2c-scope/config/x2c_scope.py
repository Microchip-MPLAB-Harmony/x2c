# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

x2cScopeCommInterfaceTypes     =  ["UART"]

global x2cScopeUartId
global x2cScopeUartBaudRateSymbolName

def x2cScopeBaudRateDep(symbol,event):
    Database.setSymbolValue(x2cScopeUartId.getValue(), x2cScopeUartBaudRateSymbolName.getValue(), event["value"])

    
    

def onAttachmentConnected(source, target):

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    
    srcID = source["id"]
    targetID = target["id"]
    
    
    if (srcID == "x2cScopeUartDependency"):
        periph_name = Database.getSymbolValue(remoteID, "USART_PLIB_API_PREFIX")
        localComponent.getSymbolByID("X2C_SCOPE_PERIPH_USED").setValue("UART")
        localComponent.getSymbolByID("X2C_SCOPE_PERIPH_USED").clearValue()
        localComponent.getSymbolByID("X2C_SCOPE_PERIPH_USED").setValue(periph_name)
        Database.setSymbolValue(remoteID, "USART_INTERRUPT_MODE", False)
        Database.setSymbolValue(remoteID, x2cScopeUartBaudRateSymbolName.getValue(), localComponent.getSymbolByID("X2C_SCOPE_BAUD_RATE").getValue())
        x2cScopeUartId.setValue(remoteID)

        

def onAttachmentDisconnected(source, target):
    
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    srcID = source["id"]
    targetID = target["id"]

    if (srcID == "x2cScopeUartDependency"):
        localComponent.getSymbolByID("X2C_SCOPE_PERIPH_USED").clearValue()
 

def setPeriphUsed(symbol, event):
    component = symbol.getComponent()
    if (event["value"] == "UART"):
        component.setDependencyEnabled("x2cScopeUartDependency", True)
        
        

################################################################################
#### Component ####
################################################################################
def instantiateComponent(x2cScopecomponent):

    global x2cScopeUartId
    global x2cScopeUartBaudRateSymbolName
    configName = Variables.get("__CONFIGURATION_NAME")
    
    x2cScopeCommInterface = x2cScopecomponent.createComboSymbol("X2C_COMM_INT", None, x2cScopeCommInterfaceTypes)
    x2cScopeCommInterface.setLabel("Communication Interface")
    x2cScopeCommInterface.setDefaultValue("UART")
   # x2cScopeCommInterface.setDependencies(setPeriphUsed, ["X2C_COMM_INT"])
    
    
    x2cScopePeriphUsed = x2cScopecomponent.createStringSymbol("X2C_SCOPE_PERIPH_USED", None)
    x2cScopePeriphUsed.setValue(x2cScopeCommInterface.getValue())
    x2cScopePeriphUsed.setVisible(False)

    
    x2cScopeBaudRate = x2cScopecomponent.createIntegerSymbol("X2C_SCOPE_BAUD_RATE", None)
    x2cScopeBaudRate.setLabel("Baud Rate")
    x2cScopeBaudRate.setDefaultValue(115200)
    
    x2cScopeBaudRateDummy = x2cScopecomponent.createIntegerSymbol("X2C_SCOPE_BAUD_RATE_DUMMY", None)
    x2cScopeBaudRateDummy.setVisible(False)
    x2cScopeBaudRateDummy.setDependencies(x2cScopeBaudRateDep, ["X2C_SCOPE_BAUD_RATE"])
    
    x2cScopeUartId = x2cScopecomponent.createStringSymbol("X2C_SCOPE_UART_ID", None)
    x2cScopeUartId.setVisible(False)
        
    print (Variables.get("__PROCESSOR"))
    
    # Include Library Files    
    if( ("SAME7" in Variables.get("__PROCESSOR")) or ("SAMV7" in Variables.get("__PROCESSOR")) or ("SAMS7" in Variables.get("__PROCESSOR"))):
        x2cScopeLibraryFile = x2cScopecomponent.createLibrarySymbol("LIB_CORTEXM7_X2C_SCOPE_A", None)
        x2cScopeLibraryFile.setSourcePath("/library/lib/libCORTEXM7_X2CScope.a")
        x2cScopeLibraryFile.setOutputName("libCORTEXM7_X2CScope.a")
        x2cScopeLibraryFile.setDestPath("/X2CCode/X2CScope/lib/")
        x2cScopeUartBaudRateSymbolName = x2cScopecomponent.createStringSymbol("X2C_SCOPE_UART_BAUD_RATE_SYMBOL", None)
        x2cScopeUartBaudRateSymbolName.setVisible(False)
        x2cScopeUartBaudRateSymbolName.setValue("BAUD_RATE")
        Log.writeInfoMessage("Cortex M7 Device Detected")
        Log.writeInfoMessage("Please ensure X2C Scope Plugin is installed from MPLABX Plugin Manager ")        
        
    elif("PIC32MK" in Variables.get("__PROCESSOR")):
        x2cScopeLibraryFile = x2cScopecomponent.createLibrarySymbol("LIB_PIC32MK_X2C_SCOPE_A", None)
        x2cScopeLibraryFile.setSourcePath("/library/lib/libPIC32MK_X2CScope.a")
        x2cScopeLibraryFile.setOutputName("libPIC32MK_X2CScope.a")
        x2cScopeLibraryFile.setDestPath("/X2CCode/X2CScope/lib/")
        x2cScopeUartBaudRateSymbolName = x2cScopecomponent.createStringSymbol("X2C_SCOPE_UART_BAUD_RATE_SYMBOL", None)
        x2cScopeUartBaudRateSymbolName.setVisible(False)
        x2cScopeUartBaudRateSymbolName.setValue("BAUD_RATE")
        Log.writeInfoMessage("MIPS M14K Device Detected")        
        Log.writeInfoMessage("Please ensure X2C Scope Plugin is installed from MPLABX Plugin Manager ")        
        
    elif( ("SAMD2" in Variables.get("__PROCESSOR")) or ("SAMC2" in Variables.get("__PROCESSOR")) or ("SAML2" in Variables.get("__PROCESSOR"))):
        x2cScopeLibraryFile = x2cScopecomponent.createLibrarySymbol("LIB_CORTEXM0PLUS_X2C_SCOPE_A", None)
        x2cScopeLibraryFile.setSourcePath("/library/lib/libCORTEXM0PLUS_X2CScope.a")
        x2cScopeLibraryFile.setOutputName("libCORTEXM0PLUS_X2CScope.a")
        x2cScopeLibraryFile.setDestPath("/X2CCode/X2CScope/lib/")
        x2cScopeUartBaudRateSymbolName = x2cScopecomponent.createStringSymbol("X2C_SCOPE_UART_BAUD_RATE_SYMBOL", None)
        x2cScopeUartBaudRateSymbolName.setVisible(False)
        x2cScopeUartBaudRateSymbolName.setValue("USART_BAUD_RATE")
        Log.writeInfoMessage("Cortex M0+ Device Detected")
        Log.writeInfoMessage("Please ensure X2C Scope Plugin is installed from MPLABX Plugin Manager ")
    
    elif( ("SAMD5" in Variables.get("__PROCESSOR")) or ("SAME5" in Variables.get("__PROCESSOR"))):
        x2cScopeLibraryFile = x2cScopecomponent.createLibrarySymbol("LIB_CORTEXM4_X2C_SCOPE_A", None)
        x2cScopeLibraryFile.setSourcePath("/library/lib/libCORTEXM4_X2CScope.a")
        x2cScopeLibraryFile.setOutputName("libCORTEXM4_X2CScope.a")
        x2cScopeLibraryFile.setDestPath("/X2CCode/X2CScope/lib/")
        x2cScopeUartBaudRateSymbolName = x2cScopecomponent.createStringSymbol("X2C_SCOPE_UART_BAUD_RATE_SYMBOL", None)
        x2cScopeUartBaudRateSymbolName.setVisible(False)
        x2cScopeUartBaudRateSymbolName.setValue("USART_BAUD_RATE")        
        Log.writeInfoMessage("Cortex M4 Device Detected")        
        Log.writeInfoMessage("Please ensure X2C Scope Plugin is installed from MPLABX Plugin Manager ")                
        
    elif("PIC32MX" in Variables.get("__PROCESSOR")):
        x2cScopeLibraryFile = x2cScopecomponent.createLibrarySymbol("LIB_PIC32MX_X2C_SCOPE_A", None)
        x2cScopeLibraryFile.setSourcePath("/library/lib/libPIC32MX_X2CScope.a")
        x2cScopeLibraryFile.setOutputName("libPIC32MX_X2CScope.a")
        x2cScopeLibraryFile.setDestPath("/X2CCode/X2CScope/lib/")
        x2cScopeUartBaudRateSymbolName = x2cScopecomponent.createStringSymbol("X2C_SCOPE_UART_BAUD_RATE_SYMBOL", None)
        x2cScopeUartBaudRateSymbolName.setVisible(False)
        x2cScopeUartBaudRateSymbolName.setValue("BAUD_RATE")        
        Log.writeInfoMessage("MIPS MX Device Detected") 
        Log.writeInfoMessage("Please ensure X2C Scope Plugin is installed from MPLABX Plugin Manager ")        

    elif("PIC32MZ" in Variables.get("__PROCESSOR")):
        x2cScopeLibraryFile = x2cScopecomponent.createLibrarySymbol("LIB_PIC32MZ_X2C_SCOPE_A", None)
        x2cScopeLibraryFile.setSourcePath("/library/lib/libPIC32MZ_X2CScope.a")
        x2cScopeLibraryFile.setOutputName("libPIC32MZ_X2CScope.a")
        x2cScopeLibraryFile.setDestPath("/X2CCode/X2CScope/lib/")
        x2cScopeUartBaudRateSymbolName = x2cScopecomponent.createStringSymbol("X2C_SCOPE_UART_BAUD_RATE_SYMBOL", None)
        x2cScopeUartBaudRateSymbolName.setVisible(False)
        x2cScopeUartBaudRateSymbolName.setValue("BAUD_RATE")        
        Log.writeInfoMessage("MIPS MZ Device Detected")
        Log.writeInfoMessage("Please ensure X2C Scope Plugin is installed from MPLABX Plugin Manager ")        


    else:
        Log.writeInfoMessage("Device Not Supported by X2C Scope")
        
        
#Include Source Files
    configName = Variables.get("__CONFIGURATION_NAME")
    
    x2cScopeSourceFile = x2cScopecomponent.createFileSymbol("X2C_SCOPE_C", None)
    x2cScopeSourceFile.setSourcePath("/library/src/X2CScope.c")
    x2cScopeSourceFile.setOutputName("X2CScope.c")
    x2cScopeSourceFile.setDestPath("/X2CCode/X2CScope/src")
    x2cScopeSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CScope/")
    x2cScopeSourceFile.setType("SOURCE")
    x2cScopeSourceFile.setOverwrite(True)
    x2cScopeSourceFile.setEnabled(True) 
    x2cScopeSourceFile.setMarkup(True)
    
    x2cScopeSourceFile = x2cScopecomponent.createFileSymbol("X2C_SCOPE_COMMUNICATION_C", None)
    x2cScopeSourceFile.setSourcePath("/templates/X2CScopeCommunication.c.ftl")
    x2cScopeSourceFile.setOutputName("X2CScopeCommunication.c")
    x2cScopeSourceFile.setDestPath("/X2CCode/X2CScope/src/")
    x2cScopeSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CScope/")
    x2cScopeSourceFile.setType("SOURCE")
    x2cScopeSourceFile.setOverwrite(True)
    x2cScopeSourceFile.setEnabled(True) 
    x2cScopeSourceFile.setMarkup(True)    
    
#Include Header Files

    x2cScopeSourceFile = x2cScopecomponent.createFileSymbol("X2C_SCOPE_H", None)
    x2cScopeSourceFile.setSourcePath("/library/inc/X2CScope.h")
    x2cScopeSourceFile.setOutputName("X2CScope.h")
    x2cScopeSourceFile.setDestPath("/X2CCode/X2CScope/inc/")
    x2cScopeSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CScope/")
    x2cScopeSourceFile.setType("HEADER")
    x2cScopeSourceFile.setOverwrite(True)
    x2cScopeSourceFile.setEnabled(True) 
    x2cScopeSourceFile.setMarkup(True)

    x2cScopeSourceFile = x2cScopecomponent.createFileSymbol("X2C_SCOPE_COMMUNICATION_H", None)
    x2cScopeSourceFile.setSourcePath("/library/inc/X2CScopeCommunication.h")
    x2cScopeSourceFile.setOutputName("X2CScopeCommunication.h")
    x2cScopeSourceFile.setDestPath("/X2CCode/X2CScope/inc/")
    x2cScopeSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CScope/")
    x2cScopeSourceFile.setType("HEADER")
    x2cScopeSourceFile.setOverwrite(True)
    x2cScopeSourceFile.setEnabled(True) 
    x2cScopeSourceFile.setMarkup(True)     
    
    # Generate Initialization File


    x2c_scope_InitFile = x2cScopecomponent.createFileSymbol("INITIALIZATION_X2C_SCOPE_C", None)
    x2c_scope_InitFile.setType("STRING")
    x2c_scope_InitFile.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE")
    x2c_scope_InitFile.setSourcePath("templates/system/initialization.c.ftl")
    x2c_scope_InitFile.setMarkup(True)

    x2cScopeSystemDefFile = x2cScopecomponent.createFileSymbol("X2C_SCOPE_SYS_DEF_HEADER", None)
    x2cScopeSystemDefFile.setType("STRING")
    x2cScopeSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    x2cScopeSystemDefFile.setSourcePath("templates/system/definitions.h.ftl")
    x2cScopeSystemDefFile.setMarkup(True)
    
    #include directories
    x2c_scope_include = x2cScopecomponent.createSettingSymbol("X2C_SCOPE_INCLUDE", None)
    x2c_scope_include.setCategory("C32")
    x2c_scope_include.setKey("extra-include-directories")
    x2c_scope_include.setValue("../src/config/"+ configName + "/X2CCode")
    x2c_scope_include.setAppend(True, ";")
    


