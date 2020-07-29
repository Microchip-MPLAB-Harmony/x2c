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
import os
global x2cModelCommInterface

x2cModelCommInterfaceTypes     =  ["UART", "USB-CDC", "TCP/IP"]


def onAttachmentConnected(source, target):

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    srcID = source["id"]
    targetID = target["id"]
    
    
    if (srcID == "x2cModelUartDependency"):
        periph_name = Database.getSymbolValue(remoteID, "USART_PLIB_API_PREFIX")
        localComponent.getSymbolByID("X2C_MODEL_PERIPH_USED").setValue("UART")
        localComponent.getSymbolByID("X2C_MODEL_PERIPH_USED").clearValue()
        localComponent.getSymbolByID("X2C_MODEL_PERIPH_USED").setValue(periph_name)
        Database.setSymbolValue(remoteID, "USART_INTERRUPT_MODE", False)
        Database.setSymbolValue(remoteID, "BAUD_RATE", 115200)

def onAttachmentDisconnected(source, target):
    
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    srcID = source["id"]
    targetID = target["id"]

    if (srcID == "x2cModelUartDependency"):
        localComponent.getSymbolByID("X2C_MODEL_PERIPH_USED").clearValue()
 



def onCommunicationInterface_Select(X2CScilabCommInterfaceSelected, event):
    if (X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_MODEL_COMM_INT").getValue() == "USB-CDC"):
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_CIRCULARBYTEBUFFER_C").setEnabled(True)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONCDC_C").setEnabled(True)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONCDC_H").setEnabled(True)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONUART_C").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONUART_H").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONTCPIP_C").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONTCPIP_H").setEnabled(False)        
    elif (X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_MODEL_COMM_INT").getValue() == "TCP/IP"):
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_CIRCULARBYTEBUFFER_C").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONCDC_C").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONCDC_H").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONUART_C").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONUART_H").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONTCPIP_C").setEnabled(True)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONTCPIP_H").setEnabled(True)            
    else:
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_CIRCULARBYTEBUFFER_C").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONCDC_C").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONCDC_H").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONUART_C").setEnabled(True)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONUART_H").setEnabled(True)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONTCPIP_C").setEnabled(False)
        X2CScilabCommInterfaceSelected.getComponent().getSymbolByID("X2C_COMMUNICATIONTCPIP_H").setEnabled(False)         
        

################################################################################
#### Component ####
################################################################################
def instantiateComponent(x2cModelcomponent):
    Log.writeInfoMessage("Running X2C Model")
    configName = Variables.get("__CONFIGURATION_NAME")
    
        #X2C Configuration Menu
    x2cModelSymMenu = x2cModelcomponent.createMenuSymbol("X2C_MODEL_MENU", None)
    x2cModelSymMenu.setLabel("X2C Model Configuration")
    x2cModelSymMenu.setDescription("Select Communication Interface and Scope Size")
    
    x2cModelCommInterface = x2cModelcomponent.createComboSymbol("X2C_MODEL_COMM_INT", x2cModelSymMenu, x2cModelCommInterfaceTypes)
    x2cModelCommInterface.setLabel("Communication Interface")
    x2cModelCommInterface.setDefaultValue("UART")
    x2cModelCommInterface.setDependencies(onCommunicationInterface_Select, ["X2C_MODEL_COMM_INT"])
    
    
    x2cModelPeriphUsed = x2cModelcomponent.createStringSymbol("X2C_MODEL_PERIPH_USED", None)
    x2cModelPeriphUsed.setValue(x2cModelCommInterface.getValue())
    x2cModelPeriphUsed.setVisible(False)
    
    X2CSym_ScopeSize = x2cModelcomponent.createIntegerSymbol("X2C_MODEL_SCOPE_SIZE", x2cModelSymMenu)
    X2CSym_ScopeSize.setLabel("Scope Size")
    X2CSym_ScopeSize.setDescription("X2C Scope Size")
    X2CSym_ScopeSize.setMin(0)
    X2CSym_ScopeSize.setMax(10000)
    X2CSym_ScopeSize.setDefaultValue(4096)
        
    
    
    ############################################################################
    #### Code Generation ####
    ############################################################################    
        
    configName = Variables.get("__CONFIGURATION_NAME")

    x2cBasicModelFile = x2cModelcomponent.createFileSymbol("X2C_BASICMODEL_ZCOS", None)
    x2cBasicModelFile.setSourcePath("/templates/basicModel.zcos")
    x2cBasicModelFile.setOutputName("basicModel.zcos")
    x2cBasicModelFile.setDestPath("/X2CCode/X2CModel/")
    x2cBasicModelFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cBasicModelFile.setType("OTHER")
    x2cBasicModelFile.setOverwrite(False)
    x2cBasicModelFile.setMarkup(False)    

    x2cFlashTableHeaderFile = x2cModelcomponent.createFileSymbol("X2C_FLASHTABLE_H", None)
    x2cFlashTableHeaderFile.setSourcePath("/templates/FlashTable.h")
    x2cFlashTableHeaderFile.setOutputName("FlashTable.h")
    x2cFlashTableHeaderFile.setDestPath("/X2CCode/X2CModel/")
    x2cFlashTableHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cFlashTableHeaderFile.setType("HEADER")
    x2cFlashTableHeaderFile.setOverwrite(False)
    x2cFlashTableHeaderFile.setMarkup(False)
	
    x2cRamTableHeaderFile = x2cModelcomponent.createFileSymbol("X2C_RAMTABLE_H", None)
    x2cRamTableHeaderFile.setSourcePath("/templates/RamTable.h")
    x2cRamTableHeaderFile.setOutputName("RamTable.h")
    x2cRamTableHeaderFile.setDestPath("/X2CCode/X2CModel/")
    x2cRamTableHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cRamTableHeaderFile.setType("HEADER")
    x2cRamTableHeaderFile.setOverwrite(False)
    x2cRamTableHeaderFile.setMarkup(False)
   

    x2cSourceFile = x2cModelcomponent.createFileSymbol("X2C_C", None)
    x2cSourceFile.setSourcePath("/templates/X2C.c.ftl")
    x2cSourceFile.setOutputName("X2C.c")
    x2cSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cSourceFile.setType("SOURCE")
    x2cSourceFile.setOverwrite(False)
    x2cSourceFile.setEnabled(True) 
    x2cSourceFile.setMarkup(True)
    
    x2cSourceFile = x2cModelcomponent.createFileSymbol("X2C_H", None)
    x2cSourceFile.setSourcePath("/templates/X2C.h.ftl")
    x2cSourceFile.setOutputName("X2C.h")
    x2cSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cSourceFile.setType("HEADER")
    x2cSourceFile.setOverwrite(False)
    x2cSourceFile.setEnabled(True) 
    x2cSourceFile.setMarkup(True)    
    
    x2cFlashTableSourceFile = x2cModelcomponent.createFileSymbol("X2C_FLASHTABLE_C", None)
    x2cFlashTableSourceFile.setSourcePath("/templates/FlashTable.c.ftl")
    x2cFlashTableSourceFile.setOutputName("FlashTable.c")
    x2cFlashTableSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cFlashTableSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cFlashTableSourceFile.setType("SOURCE")
    x2cFlashTableSourceFile.setOverwrite(False)
    x2cFlashTableSourceFile.setEnabled(True) 
    x2cFlashTableSourceFile.setMarkup(True)    

    x2cRamTableSourceFile = x2cModelcomponent.createFileSymbol("X2C_RAMTABLE_C", None)
    x2cRamTableSourceFile.setSourcePath("/templates/RamTable.c.ftl")
    x2cRamTableSourceFile.setOutputName("RamTable.c")
    x2cRamTableSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cRamTableSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cRamTableSourceFile.setType("SOURCE")
    x2cRamTableSourceFile.setOverwrite(False)
    x2cRamTableSourceFile.setEnabled(True) 
    x2cRamTableSourceFile.setMarkup(True)       

    x2cConfigX2CSourceFile = x2cModelcomponent.createFileSymbol("X2C_CONFIG_X2C_C", None)
    x2cConfigX2CSourceFile.setSourcePath("/templates/ConfigX2C.c.ftl")
    x2cConfigX2CSourceFile.setOutputName("ConfigX2C.c")
    x2cConfigX2CSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cConfigX2CSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cConfigX2CSourceFile.setType("SOURCE")
    x2cConfigX2CSourceFile.setOverwrite(False)
    x2cConfigX2CSourceFile.setEnabled(True) 
    x2cConfigX2CSourceFile.setMarkup(True)    

    x2cConfigX2CSourceFile = x2cModelcomponent.createFileSymbol("X2C_CONFIG_X2C_H", None)
    x2cConfigX2CSourceFile.setSourcePath("/templates/ConfigX2C.h.ftl")
    x2cConfigX2CSourceFile.setOutputName("ConfigX2C.h")
    x2cConfigX2CSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cConfigX2CSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cConfigX2CSourceFile.setType("HEADER")
    x2cConfigX2CSourceFile.setOverwrite(False)
    x2cConfigX2CSourceFile.setEnabled(True) 
    x2cConfigX2CSourceFile.setMarkup(True)        
    
    x2cPortConfigX2CSourceFile = x2cModelcomponent.createFileSymbol("X2C_PORTCONFIG_X2C_C", None)
    x2cPortConfigX2CSourceFile.setSourcePath("/templates/PortConfigX2C.c.ftl")
    x2cPortConfigX2CSourceFile.setOutputName("PortConfigX2C.c")
    x2cPortConfigX2CSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cPortConfigX2CSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cPortConfigX2CSourceFile.setType("SOURCE")
    x2cPortConfigX2CSourceFile.setOverwrite(False)
    x2cPortConfigX2CSourceFile.setEnabled(True) 
    x2cPortConfigX2CSourceFile.setMarkup(True)    
    
    x2cPortConfigX2CSourceFile = x2cModelcomponent.createFileSymbol("X2C_PORTCONFIG_X2C_H", None)
    x2cPortConfigX2CSourceFile.setSourcePath("/templates/PortConfigX2C.h.ftl")
    x2cPortConfigX2CSourceFile.setOutputName("PortConfigX2C.h")
    x2cPortConfigX2CSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cPortConfigX2CSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cPortConfigX2CSourceFile.setType("HEADER")
    x2cPortConfigX2CSourceFile.setOverwrite(False)
    x2cPortConfigX2CSourceFile.setEnabled(True) 
    x2cPortConfigX2CSourceFile.setMarkup(True)

    x2cCommunicationUartSourceFile = x2cModelcomponent.createFileSymbol("X2C_COMMUNICATIONUART_C", None)
    x2cCommunicationUartSourceFile.setSourcePath("/templates/CommunicationUart.c.ftl")
    x2cCommunicationUartSourceFile.setOutputName("CommunicationUart.c")
    x2cCommunicationUartSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cCommunicationUartSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cCommunicationUartSourceFile.setType("SOURCE")
    x2cCommunicationUartSourceFile.setOverwrite(True)
    x2cCommunicationUartSourceFile.setEnabled(True) 
    x2cCommunicationUartSourceFile.setMarkup(True)    

    x2cCommunicationUartSourceFile = x2cModelcomponent.createFileSymbol("X2C_COMMUNICATIONUART_H", None)
    x2cCommunicationUartSourceFile.setSourcePath("/templates/CommunicationUart.h.ftl")
    x2cCommunicationUartSourceFile.setOutputName("CommunicationUart.h")
    x2cCommunicationUartSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cCommunicationUartSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cCommunicationUartSourceFile.setType("HEADER")
    x2cCommunicationUartSourceFile.setOverwrite(True)
    x2cCommunicationUartSourceFile.setEnabled(True) 
    x2cCommunicationUartSourceFile.setMarkup(True) 
    
    x2cCommunicationUSBCDCSourceFile = x2cModelcomponent.createFileSymbol("X2C_COMMUNICATIONCDC_C", None)
    x2cCommunicationUSBCDCSourceFile.setSourcePath("/templates/CommunicationCDC.c.ftl")
    x2cCommunicationUSBCDCSourceFile.setOutputName("CommunicationCDC.c")
    x2cCommunicationUSBCDCSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cCommunicationUSBCDCSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cCommunicationUSBCDCSourceFile.setType("SOURCE")
    x2cCommunicationUSBCDCSourceFile.setOverwrite(True)
    x2cCommunicationUSBCDCSourceFile.setEnabled(False) 
    x2cCommunicationUSBCDCSourceFile.setMarkup(True)    

    x2cCommunicationUSBCDCSourceFile = x2cModelcomponent.createFileSymbol("X2C_COMMUNICATIONCDC_H", None)
    x2cCommunicationUSBCDCSourceFile.setSourcePath("/templates/CommunicationCDC.h.ftl")
    x2cCommunicationUSBCDCSourceFile.setOutputName("CommunicationCDC.h")
    x2cCommunicationUSBCDCSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cCommunicationUSBCDCSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cCommunicationUSBCDCSourceFile.setType("HEADER")
    x2cCommunicationUSBCDCSourceFile.setOverwrite(True)
    x2cCommunicationUSBCDCSourceFile.setEnabled(False) 
    x2cCommunicationUSBCDCSourceFile.setMarkup(True)

    x2cCommunicationTCPIPSourceFile = x2cModelcomponent.createFileSymbol("X2C_COMMUNICATIONTCPIP_C", None)
    x2cCommunicationTCPIPSourceFile.setSourcePath("/templates/CommunicationTCPIP.c.ftl")
    x2cCommunicationTCPIPSourceFile.setOutputName("CommunicationTCPIP.c")
    x2cCommunicationTCPIPSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cCommunicationTCPIPSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cCommunicationTCPIPSourceFile.setType("SOURCE")
    x2cCommunicationTCPIPSourceFile.setOverwrite(True)
    x2cCommunicationTCPIPSourceFile.setEnabled(False) 
    x2cCommunicationTCPIPSourceFile.setMarkup(True)    

    x2cCommunicationTCPIPHeaderFile = x2cModelcomponent.createFileSymbol("X2C_COMMUNICATIONTCPIP_H", None)
    x2cCommunicationTCPIPHeaderFile.setSourcePath("/templates/CommunicationTCPIP.h.ftl")
    x2cCommunicationTCPIPHeaderFile.setOutputName("CommunicationTCPIP.h")
    x2cCommunicationTCPIPHeaderFile.setDestPath("/X2CCode/X2CModel/")
    x2cCommunicationTCPIPHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cCommunicationTCPIPHeaderFile.setType("HEADER")
    x2cCommunicationTCPIPHeaderFile.setOverwrite(True)
    x2cCommunicationTCPIPHeaderFile.setEnabled(False) 
    x2cCommunicationTCPIPHeaderFile.setMarkup(True)    
    
    x2c_model_InitFile = x2cModelcomponent.createFileSymbol("INITIALIZATION_X2C_MODEL_C", None)
    x2c_model_InitFile.setType("STRING")
    x2c_model_InitFile.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE")
    x2c_model_InitFile.setSourcePath("templates/system/initialization.c.ftl")
    x2c_model_InitFile.setMarkup(True)
    
    x2cModelSystemDefFile = x2cModelcomponent.createFileSymbol("X2C_MODEL_SYS_DEF_HEADER", None)
    x2cModelSystemDefFile.setType("STRING")
    x2cModelSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    x2cModelSystemDefFile.setSourcePath("templates/system/definitions.h.ftl")
    x2cModelSystemDefFile.setMarkup(True)
	
#Include Library Files    

    x2cScope_MainSourceFile = x2cModelcomponent.createFileSymbol("X2C_SCOPE_MAIN_C", None)
    x2cScope_MainSourceFile.setSourcePath("../../x2c_installer_files/Library/General/Controller/src/Scope_Main.c")
    x2cScope_MainSourceFile.setOutputName("Scope_Main.c")
    x2cScope_MainSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cScope_MainSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cScope_MainSourceFile.setType("SOURCE")
    x2cScope_MainSourceFile.setMarkup(False)
    
    if( ("SAME7" in Variables.get("__PROCESSOR")) or ("SAMS7" in Variables.get("__PROCESSOR")) or ("SAMV7" in Variables.get("__PROCESSOR"))):
        x2cGeneralLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_GENERAL_LIB_SAME70_A", None)
        x2cGeneralLibraryFile.setSourcePath("../../x2c_installer_files/Library/General/Controller/lib/libCortexM7-ATSAM_General.a")
        x2cGeneralLibraryFile.setOutputName("libCortexM7-ATSAM_General.a")
        x2cGeneralLibraryFile.setDestPath("/X2CCode/X2CModel/Library/General/Controller/lib/")
        
        x2cControlLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_CONTROL_LIB_SAME70_A", None)
        x2cControlLibraryFile.setSourcePath("../../x2c_installer_files/Library/Control/Controller/lib/libCortexM7-ATSAM_Control.a")
        x2cControlLibraryFile.setOutputName("libCortexM7-ATSAM_Control.a")
        x2cControlLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Control/Controller/lib/")

        x2cMathLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MATH_LIB_SAME70_A", None)
        x2cMathLibraryFile.setSourcePath("../../x2c_installer_files/Library/Math/Controller/lib/libCortexM7-ATSAM_Math.a")
        x2cMathLibraryFile.setOutputName("libCortexM7-ATSAM_Math.a")
        x2cMathLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Math/Controller/lib/")
        
        x2cMCHPLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MCHP_LIB_SAME70_A", None)
        x2cMCHPLibraryFile.setSourcePath("../../x2c_installer_files/Library/MCHP/Controller/lib/libCortexM7-ATSAM_MCHP.a")
        x2cMCHPLibraryFile.setOutputName("libCortexM7-ATSAM_MCHP.a")
        x2cMCHPLibraryFile.setDestPath("/X2CCode/X2CModel/Library/MCHP/Controller/lib/")
    
    elif( ("PIC32CM" in Variables.get("__PROCESSOR")) or ("SAMD2" in Variables.get("__PROCESSOR")) or ("SAMC2" in Variables.get("__PROCESSOR")) or ("SAML2" in Variables.get("__PROCESSOR"))):
        x2cGeneralLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_GENERAL_LIB_SAMC21_A", None)
        x2cGeneralLibraryFile.setSourcePath("../../x2c_installer_files/Library/General/Controller/lib/libCortexM0Plus-ATSAM_General.a")
        x2cGeneralLibraryFile.setOutputName("libCortexM0Plus-ATSAM_General.a")
        x2cGeneralLibraryFile.setDestPath("/X2CCode/X2CModel/Library/General/Controller/lib/")
        
        x2cControlLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_CONTROL_LIB_SAMC21_A", None)
        x2cControlLibraryFile.setSourcePath("../../x2c_installer_files/Library/Control/Controller/lib/libCortexM0Plus-ATSAM_Control.a")
        x2cControlLibraryFile.setOutputName("libCortexM0Plus-ATSAM_Control.a")
        x2cControlLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Control/Controller/lib/")

        x2cMathLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MATH_LIB_SAMC21_A", None)
        x2cMathLibraryFile.setSourcePath("../../x2c_installer_files/Library/Math/Controller/lib/libCortexM0Plus-ATSAM_Math.a")
        x2cMathLibraryFile.setOutputName("libCortexM0Plus-ATSAM_Math.a")
        x2cMathLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Math/Controller/lib/")
        
        x2cMCHPLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MCHP_LIB_SAMC21_A", None)
        x2cMCHPLibraryFile.setSourcePath("../../x2c_installer_files/Library/MCHP/Controller/lib/libCortexM0Plus-ATSAM_MCHP.a")
        x2cMCHPLibraryFile.setOutputName("libCortexM0Plus-ATSAM_MCHP.a")
        x2cMCHPLibraryFile.setDestPath("/X2CCode/X2CModel/Library/MCHP/Controller/lib/")   

    elif( ("SAMD5" in Variables.get("__PROCESSOR")) or ("SAME5" in Variables.get("__PROCESSOR"))):
        x2cGeneralLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_GENERAL_LIB_SAME54_A", None)
        x2cGeneralLibraryFile.setSourcePath("../../x2c_installer_files/Library/General/Controller/lib/libCortexM4-ATSAM_General.a")
        x2cGeneralLibraryFile.setOutputName("libCortexM4-ATSAM_General.a")
        x2cGeneralLibraryFile.setDestPath("/X2CCode/X2CModel/Library/General/Controller/lib/")
        
        x2cControlLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_CONTROL_LIB_SAME54_A", None)
        x2cControlLibraryFile.setSourcePath("../../x2c_installer_files/Library/Control/Controller/lib/libCortexM4-ATSAM_Control.a")
        x2cControlLibraryFile.setOutputName("libCortexM4-ATSAM_Control.a")
        x2cControlLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Control/Controller/lib/")

        x2cMathLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MATH_LIB_SAME54_A", None)
        x2cMathLibraryFile.setSourcePath("../../x2c_installer_files/Library/Math/Controller/lib/libCortexM4-ATSAM_Math.a")
        x2cMathLibraryFile.setOutputName("libCortexM4-ATSAM_Math.a")
        x2cMathLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Math/Controller/lib/")
        
        x2cMCHPLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MCHP_LIB_SAME54_A", None)
        x2cMCHPLibraryFile.setSourcePath("../../x2c_installer_files/Library/MCHP/Controller/lib/libCortexM4-ATSAM_MCHP.a")
        x2cMCHPLibraryFile.setOutputName("libCortexM4-ATSAM_MCHP.a")
        x2cMCHPLibraryFile.setDestPath("/X2CCode/X2CModel/Library/MCHP/Controller/lib/")              

    elif("PIC32MX" in Variables.get("__PROCESSOR")):
        x2cGeneralLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_GENERAL_A_PIC32MX_A", None)
        x2cGeneralLibraryFile.setSourcePath("../../x2c_installer_files/Library/General/Controller/lib/libPIC32MX_General.a")
        x2cGeneralLibraryFile.setOutputName("libPIC32MX_General.a")
        x2cGeneralLibraryFile.setDestPath("/X2CCode/X2CModel/Library/General/Controller/lib/")
        
        x2cControlLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_CONTROL_A_PIC32MX_A", None)
        x2cControlLibraryFile.setSourcePath("../../x2c_installer_files/Library/Control/Controller/lib/libPIC32MX_Control.a")
        x2cControlLibraryFile.setOutputName("libPIC32MX_Control.a")
        x2cControlLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Control/Controller/lib/")

        x2cMathLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MATH_A_PIC32MX_A", None)
        x2cMathLibraryFile.setSourcePath("../../x2c_installer_files/Library/Math/Controller/lib/libPIC32MX_Math.a")
        x2cMathLibraryFile.setOutputName("libPIC32MX_Math.a")
        x2cMathLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Math/Controller/lib/")
        
        x2cMCHPLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MCHP_A_PIC32MX_A", None)
        x2cMCHPLibraryFile.setSourcePath("../../x2c_installer_files/Library/MCHP/Controller/lib/libPIC32MX_MCHP.a")
        x2cMCHPLibraryFile.setOutputName("libPIC32MX_MCHP.a")
        x2cMCHPLibraryFile.setDestPath("/X2CCode/X2CModel/Library/MCHP/Controller/lib/")

    elif("PIC32MZ" in Variables.get("__PROCESSOR")):
        x2cGeneralLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_GENERAL_A_PIC32MZ_A", None)
        x2cGeneralLibraryFile.setSourcePath("../../x2c_installer_files/Library/General/Controller/lib/libPIC32MZ_General.a")
        x2cGeneralLibraryFile.setOutputName("libPIC32MZ_General.a")
        x2cGeneralLibraryFile.setDestPath("/X2CCode/X2CModel/Library/General/Controller/lib/")
        
        x2cControlLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_CONTROL_A_PIC32MZ_A", None)
        x2cControlLibraryFile.setSourcePath("../../x2c_installer_files/Library/Control/Controller/lib/libPIC32MZ_Control.a")
        x2cControlLibraryFile.setOutputName("libPIC32MZ_Control.a")
        x2cControlLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Control/Controller/lib/")

        x2cMathLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MATH_A_PIC32MZ_A", None)
        x2cMathLibraryFile.setSourcePath("../../x2c_installer_files/Library/Math/Controller/lib/libPIC32MZ_Math.a")
        x2cMathLibraryFile.setOutputName("libPIC32MZ_Math.a")
        x2cMathLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Math/Controller/lib/")
        
        x2cMCHPLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MCHP_A_PIC32MZ_A", None)
        x2cMCHPLibraryFile.setSourcePath("../../x2c_installer_files/Library/MCHP/Controller/lib/libPIC32MZ_MCHP.a")
        x2cMCHPLibraryFile.setOutputName("libPIC32MZ_MCHP.a")
        x2cMCHPLibraryFile.setDestPath("/X2CCode/X2CModel/Library/MCHP/Controller/lib/")    

    elif("PIC32MK" in Variables.get("__PROCESSOR")):
        x2cGeneralLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_GENERAL_A_PIC32MK_A", None)
        x2cGeneralLibraryFile.setSourcePath("../../x2c_installer_files/Library/General/Controller/lib/libPIC32MK_General.a")
        x2cGeneralLibraryFile.setOutputName("libPIC32MK_General.a")
        x2cGeneralLibraryFile.setDestPath("/X2CCode/X2CModel/Library/General/Controller/lib/")
        
        x2cControlLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_CONTROL_A_PIC32MK_A", None)
        x2cControlLibraryFile.setSourcePath("../../x2c_installer_files/Library/Control/Controller/lib/libPIC32MK_Control.a")
        x2cControlLibraryFile.setOutputName("libPIC32MK_Control.a")
        x2cControlLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Control/Controller/lib/")

        x2cMathLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MATH_A_PIC32MK_A", None)
        x2cMathLibraryFile.setSourcePath("../../x2c_installer_files/Library/Math/Controller/lib/libPIC32MK_Math.a")
        x2cMathLibraryFile.setOutputName("libPIC32MK_Math.a")
        x2cMathLibraryFile.setDestPath("/X2CCode/X2CModel/Library/Math/Controller/lib/")
        
        x2cMCHPLibraryFile = x2cModelcomponent.createLibrarySymbol("X2C_MCHP_A_PIC32MK_A", None)
        x2cMCHPLibraryFile.setSourcePath("../../x2c_installer_files/Library/MCHP/Controller/lib/libPIC32MK_MCHP.a")
        x2cMCHPLibraryFile.setOutputName("libPIC32MK_MCHP.a")
        x2cMCHPLibraryFile.setDestPath("/X2CCode/X2CModel/Library/MCHP/Controller/lib/")           

#dependency files

    

    
      

    #include directories
    x2c_inc_common = x2cModelcomponent.createSettingSymbol("X2C_INC_COMMON", None)
    x2c_inc_common.setCategory("C32")
    x2c_inc_common.setKey("extra-include-directories")
    x2c_inc_common.setValue("../src/config/"+configName+"/X2CCode/X2CModel/Controller/Common")
    x2c_inc_common.setAppend(True, ";")
    
    x2c_inc_services = x2cModelcomponent.createSettingSymbol("X2C_INC_SERVICES", None)
    x2c_inc_services.setCategory("C32")
    x2c_inc_services.setKey("extra-include-directories")
    x2c_inc_services.setValue("../src/config/"+configName+"/X2CCode/X2CModel/Controller/Services")
    x2c_inc_services.setAppend(True, ";")
    
    x2c_inc_services = x2cModelcomponent.createSettingSymbol("X2C_INC_CRC", None)
    x2c_inc_services.setCategory("C32")
    x2c_inc_services.setKey("extra-include-directories")
    x2c_inc_services.setValue("../src/config/"+configName+"/X2CCode/X2CModel/Controller/CRC")
    x2c_inc_services.setAppend(True, ";")
    
    x2c_inc_lnet = x2cModelcomponent.createSettingSymbol("X2C_INC_LNET", None)
    x2c_inc_lnet.setCategory("C32")
    x2c_inc_lnet.setKey("extra-include-directories")
    x2c_inc_lnet.setValue("../src/config/"+configName+"/X2CCode/X2CModel/Controller/Protocol/LNet")
    x2c_inc_lnet.setAppend(True, ";")

    x2c_inc_driver_serial = x2cModelcomponent.createSettingSymbol("X2C_INC_DRIVER_SERIAL", None)
    x2c_inc_driver_serial.setCategory("C32")
    x2c_inc_driver_serial.setKey("extra-include-directories")
    x2c_inc_driver_serial.setValue("../src/config/"+configName+"/X2CCode/X2CModel/Controller/Driver/Serial")
    x2c_inc_driver_serial.setAppend(True, ";")

    x2c_inc_general_library = x2cModelcomponent.createSettingSymbol("X2C_INC_GENERAL_LIBRARY", None)
    x2c_inc_general_library.setCategory("C32")
    x2c_inc_general_library.setKey("extra-include-directories")
    x2c_inc_general_library.setValue("../src/config/"+configName+"/X2CCode/X2CModel/Library/General/Controller/inc")
    x2c_inc_general_library.setAppend(True, ";")


    x2c_inc_math_library = x2cModelcomponent.createSettingSymbol("X2C_INC_MATH_LIBRARY", None)
    x2c_inc_math_library.setCategory("C32")
    x2c_inc_math_library.setKey("extra-include-directories")
    x2c_inc_math_library.setValue("../src/config/"+configName+"/X2CCode/X2CModel/Library/Math/Controller/inc")
    x2c_inc_math_library.setAppend(True, ";")
    
    x2c_inc_control_library = x2cModelcomponent.createSettingSymbol("X2C_INC_CONTROL_LIBRARY", None)
    x2c_inc_control_library.setCategory("C32")
    x2c_inc_control_library.setKey("extra-include-directories")
    x2c_inc_control_library.setValue("../src/config/"+configName+"/X2CCode/X2CModel/Library/Control/Controller/inc")
    x2c_inc_control_library.setAppend(True, ";")
    
    x2c_inc_control_library = x2cModelcomponent.createSettingSymbol("X2C_INC_MCHP_LIBRARY", None)
    x2c_inc_control_library.setCategory("C32")
    x2c_inc_control_library.setKey("extra-include-directories")
    x2c_inc_control_library.setValue("../src/config/"+configName+"/X2CCode/X2CModel/Library/MCHP/Controller/inc")
    x2c_inc_control_library.setAppend(True, ";")
    
    x2c_inc_X2C = x2cModelcomponent.createSettingSymbol("X2C_INC_X2C", None)
    x2c_inc_X2C.setCategory("C32")
    x2c_inc_X2C.setKey("extra-include-directories")
    x2c_inc_X2C.setValue("../src/config/"+configName+"/X2CCode/X2CModel/")
    x2c_inc_X2C.setAppend(True, ";")

    x2c_inc_X2CCODE = x2cModelcomponent.createSettingSymbol("X2C_INC_X2CCODE", None)
    x2c_inc_X2CCODE.setCategory("C32")
    x2c_inc_X2CCODE.setKey("extra-include-directories")
    x2c_inc_X2CCODE.setValue("../src/config/"+configName+"/X2CCode/")
    x2c_inc_X2CCODE.setAppend(True, ";")

    #pre-processor symbol
    x2c_def_processor_type = x2cModelcomponent.createSettingSymbol("X2C_DEF_PROCESSOR_TYPE", None)
    x2c_def_processor_type.setCategory("C32")
    x2c_def_processor_type.setKey("preprocessor-macros")
    x2c_def_processor_type.setValue("__GENERIC_MICROCHIP_PIC32__")
    x2c_def_processor_type.setAppend(True, ";")
	
    #pre-processor symbol
    x2c_def_scope_size_type = x2cModelcomponent.createSettingSymbol("X2C_DEF_SCOPE_SIZE", None)
    x2c_def_scope_size_type.setCategory("C32")
    x2c_def_scope_size_type.setKey("preprocessor-macros")
    x2c_def_scope_size_type.setValue("SCOPE_SIZE="+str(X2CSym_ScopeSize.getValue()))
    x2c_def_scope_size_type.setAppend(True, ";")



    
	############################################################################
	## X2C/Controller/Common/
	############################################################################
    
    x2cCircularByteBufferSourceFile = x2cModelcomponent.createFileSymbol("X2C_CIRCULARBYTEBUFFER_C", None)
    x2cCircularByteBufferSourceFile.setSourcePath("../../x2c_installer_files/Controller/Common/CircularByteBuffer.c")
    x2cCircularByteBufferSourceFile.setOutputName("CircularByteBuffer.c")
    x2cCircularByteBufferSourceFile.setDestPath("/X2CCode/X2CModel/")
    x2cCircularByteBufferSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/")
    x2cCircularByteBufferSourceFile.setType("SOURCE")
    x2cCircularByteBufferSourceFile.setMarkup(False)
    x2cCircularByteBufferSourceFile.setEnabled(False)
    
    for root, dirs, files in os.walk(Module.getPath()+"../../x2c_installer_files/Controller/Common/"):
        for filename in files:
	#		if (".c" in filename):
	#			x2cSourceFile = x2cModelcomponent.createFileSymbol(str(filename), None)
	#			x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Common/" + filename)
	#			x2cSourceFile.setOutputName(filename)
	#			x2cSourceFile.setDestPath("/X2CCode/Controller/Common/")
	#			x2cSourceFile.setProjectPath("X2CCode/Controller/Common")
	#			x2cSourceFile.setType("SOURCE")
	#			x2cSourceFile.setMarkup(False)
	#
			if (".h" in filename):
				x2cHeaderFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cHeaderFile.setSourcePath("../../x2c_installer_files/Controller/Common/" + filename)
				x2cHeaderFile.setOutputName(filename)
				x2cHeaderFile.setDestPath("/X2CCode/X2CModel/Controller/Common/")
				x2cHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Common/")
				x2cHeaderFile.setType("HEADER")
				x2cHeaderFile.setMarkup(False)

	x2cSourceFile = x2cModelcomponent.createFileSymbol("X2C_TABLESTRUCT_C", None)
	x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Common/TableStruct.c")
	x2cSourceFile.setOutputName("TableStruct.c")
	x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setType("SOURCE")
	x2cSourceFile.setMarkup(False)

	x2cSourceFile = x2cModelcomponent.createFileSymbol("X2C_SQRT_DATA_C", None)
	x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Common/Sqrt_Data.c")
	x2cSourceFile.setOutputName("Sqrt_Data.c")
	x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setType("SOURCE")
	x2cSourceFile.setMarkup(False)

	x2cSourceFile = x2cModelcomponent.createFileSymbol("X2C_SIN_DATA_C", None)
	x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Common/Sin_Data.c")
	x2cSourceFile.setOutputName("Sin_Data.c")
	x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setType("SOURCE")
	x2cSourceFile.setMarkup(False)

	x2cSourceFile = x2cModelcomponent.createFileSymbol("X2C_SIN2_DATA_C", None)
	x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Common/Sin2_Data.c")
	x2cSourceFile.setOutputName("Sin2_Data.c")
	x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setType("SOURCE")
	x2cSourceFile.setMarkup(False)

	x2cSourceFile = x2cModelcomponent.createFileSymbol("X2C_EXP_DATA_C", None)
	x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Common/Exp_Data.c")
	x2cSourceFile.setOutputName("Exp_Data.c")
	x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setType("SOURCE")
	x2cSourceFile.setMarkup(False)

	x2cSourceFile = x2cModelcomponent.createFileSymbol("X2C_COMMONFCTS_C", None)
	x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Common/CommonFcts.c")
	x2cSourceFile.setOutputName("CommonFcts.c")
	x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setType("SOURCE")
	x2cSourceFile.setMarkup(False)

	x2cSourceFile = x2cModelcomponent.createFileSymbol("X2C_ATAN_DATA_C", None)
	x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Common/Atan_Data.c")
	x2cSourceFile.setOutputName("Atan_Data.c")
	x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Common/")
	x2cSourceFile.setType("SOURCE")
	x2cSourceFile.setMarkup(False)	
	############################################################################
	## X2C/Controller/CRC/
	############################################################################
	for root, dirs, files in os.walk(Module.getPath()+"../../x2c_installer_files/Controller/CRC/"):
		for filename in files:
			if (".c" in filename):
				x2cSourceFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/CRC/" + filename)
				x2cSourceFile.setOutputName(filename)
				x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/CRC/")
				x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel//Controller/CRC/")
				x2cSourceFile.setType("SOURCE")
				x2cSourceFile.setMarkup(False)

			if (".h" in filename):
				x2cHeaderFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cHeaderFile.setSourcePath("../../x2c_installer_files/Controller/CRC/" + filename)
				x2cHeaderFile.setOutputName(filename)
				x2cHeaderFile.setDestPath("/X2CCode/X2CModel/Controller/CRC/")
				x2cHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/CRC/")
				x2cHeaderFile.setType("HEADER")
				x2cHeaderFile.setMarkup(False)

	############################################################################
	## X2C/Controller/Driver/Serial/
	############################################################################
	for root, dirs, files in os.walk(Module.getPath()+"../../x2c_installer_files/Controller/Driver/Serial/"):
		for filename in files:
			if (".c" in filename):
				x2cSourceFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Driver/Serial/" + filename)
				x2cSourceFile.setOutputName(filename)
				x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Driver/Serial/")
				x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Driver/Serial")
				x2cSourceFile.setType("SOURCE")
				x2cSourceFile.setMarkup(False)

			if (".h" in filename):
				x2cHeaderFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cHeaderFile.setSourcePath("../../x2c_installer_files/Controller/Driver/Serial/" + filename)
				x2cHeaderFile.setOutputName(filename)
				x2cHeaderFile.setDestPath("/X2CCode/X2CModel/Controller/Driver/Serial")
				x2cHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Driver/Serial")
				x2cHeaderFile.setType("HEADER")
				x2cHeaderFile.setMarkup(False)

	############################################################################
	## X2C/Controller/Protocol/LNet
	############################################################################
	for root, dirs, files in os.walk(Module.getPath()+"../../x2c_installer_files/Controller/Protocol/LNet/"):
		for filename in files:
			if (".c" in filename):
				x2cSourceFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Protocol/LNet/" + filename)
				x2cSourceFile.setOutputName(filename)
				x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Protocol/LNet/")
				x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Protocol/LNet")
				x2cSourceFile.setType("SOURCE")
				x2cSourceFile.setMarkup(False)

			if (".h" in filename):
				x2cHeaderFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cHeaderFile.setSourcePath("../../x2c_installer_files/Controller/Protocol/LNet/" + filename)
				x2cHeaderFile.setOutputName(filename)
				x2cHeaderFile.setDestPath("/X2CCode/X2CModel/Controller/Protocol/LNet")
				x2cHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Protocol/LNet")
				x2cHeaderFile.setType("HEADER")
				x2cHeaderFile.setMarkup(False)
				
	############################################################################
	## X2C/Controller/Services
	############################################################################
	for root, dirs, files in os.walk(Module.getPath()+"../../x2c_installer_files/Controller/Services/"):
		for filename in files:
			if (".c" in filename):
				x2cSourceFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Services/" + filename)
				x2cSourceFile.setOutputName(filename)
				x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Services/")
				x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Services")
				x2cSourceFile.setType("SOURCE")
				x2cSourceFile.setMarkup(False)

			if (".h" in filename):
				x2cHeaderFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cHeaderFile.setSourcePath("../../x2c_installer_files/Controller/Services/" + filename)
				x2cHeaderFile.setOutputName(filename)
				x2cHeaderFile.setDestPath("/X2CCode/X2CModel/Controller/Services")
				x2cHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Services")
				x2cHeaderFile.setType("HEADER")
				x2cHeaderFile.setMarkup(False)
				
	############################################################################
	## X2C/Library/Control/Controller/inc
	############################################################################
	for root, dirs, files in os.walk(Module.getPath()+"../../x2c_installer_files/Library/Control/Controller/inc/"):
		for filename in files:
			#if (".c" in filename):
			#	x2cSourceFile = x2cModelcomponent.createFileSymbol(str(filename), None)
			#	x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Services/" + filename)
			#	x2cSourceFile.setOutputName(filename)
			#	x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Services/")
			#	x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Services")
			#	x2cSourceFile.setType("SOURCE")
			#	x2cSourceFile.setMarkup(False)

			if (".h" in filename):
				x2cHeaderFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cHeaderFile.setSourcePath("../../x2c_installer_files/Library/Control/Controller/inc/" + filename)
				x2cHeaderFile.setOutputName(filename)
				x2cHeaderFile.setDestPath("/X2CCode/X2CModel/Library/Control/Controller/inc")
				x2cHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Library/Control/Controller/inc")
				x2cHeaderFile.setType("HEADER")
				x2cHeaderFile.setMarkup(False)
				
	############################################################################
	## X2C/Library/General/Controller/inc
	############################################################################
	for root, dirs, files in os.walk(Module.getPath()+"../../x2c_installer_files/Library/General/Controller/inc/"):
		for filename in files:
			#if (".c" in filename):
			#	x2cSourceFile = x2cModelcomponent.createFileSymbol(str(filename), None)
			#	x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Services/" + filename)
			#	x2cSourceFile.setOutputName(filename)
			#	x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Services/")
			#	x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Services")
			#	x2cSourceFile.setType("SOURCE")
			#	x2cSourceFile.setMarkup(False)

			if (".h" in filename):
				x2cHeaderFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cHeaderFile.setSourcePath("../../x2c_installer_files/Library/General/Controller/inc/" + filename)
				x2cHeaderFile.setOutputName(filename)
				x2cHeaderFile.setDestPath("/X2CCode/X2CModel/Library/General/Controller/inc")
				x2cHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Library/General/Controller/inc")
				x2cHeaderFile.setType("HEADER")
				x2cHeaderFile.setMarkup(False)
				
	############################################################################
	## X2C/Library/Math/Controller/inc
	############################################################################
	for root, dirs, files in os.walk(Module.getPath()+"../../x2c_installer_files/Library/Math/Controller/inc/"):
		for filename in files:
			#if (".c" in filename):
			#	x2cSourceFile = x2cModelcomponent.createFileSymbol(str(filename), None)
			#	x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Services/" + filename)
			#	x2cSourceFile.setOutputName(filename)
			#	x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Services/")
			#	x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Services")
			#	x2cSourceFile.setType("SOURCE")
			#	x2cSourceFile.setMarkup(False)

			if (".h" in filename):
				x2cHeaderFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cHeaderFile.setSourcePath("../../x2c_installer_files/Library/Math/Controller/inc/" + filename)
				x2cHeaderFile.setOutputName(filename)
				x2cHeaderFile.setDestPath("/X2CCode/X2CModel/Library/Math/Controller/inc")
				x2cHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Library/Math/Controller/inc")
				x2cHeaderFile.setType("HEADER")
				x2cHeaderFile.setMarkup(False)

	############################################################################
	## X2C/Library/Math/Controller/inc
	############################################################################
	for root, dirs, files in os.walk(Module.getPath()+"../../x2c_installer_files/Library/MCHP/Controller/inc/"):
		for filename in files:
			#if (".c" in filename):
			#	x2cSourceFile = x2cModelcomponent.createFileSymbol(str(filename), None)
			#	x2cSourceFile.setSourcePath("../../x2c_installer_files/Controller/Services/" + filename)
			#	x2cSourceFile.setOutputName(filename)
			#	x2cSourceFile.setDestPath("/X2CCode/X2CModel/Controller/Services/")
			#	x2cSourceFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Controller/Services")
			#	x2cSourceFile.setType("SOURCE")
			#	x2cSourceFile.setMarkup(False)

			if (".h" in filename):
				x2cHeaderFile = x2cModelcomponent.createFileSymbol(str(filename), None)
				x2cHeaderFile.setSourcePath("../../x2c_installer_files/Library/MCHP/Controller/inc/" + filename)
				x2cHeaderFile.setOutputName(filename)
				x2cHeaderFile.setDestPath("/X2CCode/X2CModel/Library/MCHP/Controller/inc")
				x2cHeaderFile.setProjectPath("config/"+configName+"/X2CCode/X2CModel/Library/MCHP/Controller/inc")
				x2cHeaderFile.setType("HEADER")
				x2cHeaderFile.setMarkup(False)
