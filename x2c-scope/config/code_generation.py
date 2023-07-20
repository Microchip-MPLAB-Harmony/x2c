
"""*****************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

"""*****************************************************************************
* File Name: general_functions.py
*
* Description:
* General functions
*
*****************************************************************************"""
class X2CScope_CodeGenerationClass:
    def __init__(self, component):
        self.component = component

        MCU = Variables.get("__PROCESSOR")
        if( ("SAME7" in MCU) or ("SAMV7" in MCU) or ("SAMS7" in MCU) or ("SAMRH707" in MCU)):
            self.libraryName = "libCORTEXM7_X2CScope.a"

        elif("PIC32MK" in MCU):
            self.libraryName = "libPIC32MK_X2CScope.a"

        elif(("PIC32CM" in MCU) or ("SAMD2" in MCU) or ("SAMC2" in MCU) or ("SAML2" in MCU)):
            self.libraryName = "libCORTEXM0PLUS_X2CScope.a"

        elif( ("SAMD5" in MCU) or ("SAME5" in MCU)):
            self.libraryName = "libCORTEXM4_X2CScope.a"

        elif("PIC32MX" in MCU):
            self.libraryName = "libPIC32MX_X2CScope.a"

        elif("PIC32MZ" in MCU):
            self.libraryName = "libPIC32MZ_X2CScope.a"

    def generateCode(self):
        # Include Library Files
        sym_LIBARY_FILE = self.component.createLibrarySymbol("LIB_CORTEXM7_X2C_SCOPE_A", None)
        sym_LIBARY_FILE.setSourcePath("/library/lib/" + self.libraryName )
        sym_LIBARY_FILE.setOutputName(self.libraryName)
        sym_LIBARY_FILE.setDestPath("/X2CCode/X2CScope/lib/")

        #Include Source Files
        configName = Variables.get("__CONFIGURATION_NAME")

        sym_SOURCE_FILE = self.component.createFileSymbol("X2C_SCOPE_C", None)
        sym_SOURCE_FILE.setSourcePath("/library/src/X2CScope.c")
        sym_SOURCE_FILE.setOutputName("X2CScope.c")
        sym_SOURCE_FILE.setDestPath("/X2CCode/X2CScope/src")
        sym_SOURCE_FILE.setProjectPath("config/"+configName+"/X2CCode/X2CScope/")
        sym_SOURCE_FILE.setType("SOURCE")
        sym_SOURCE_FILE.setOverwrite(True)
        sym_SOURCE_FILE.setEnabled(True)
        sym_SOURCE_FILE.setMarkup(True)

        sym_SOURCE_FILE = self.component.createFileSymbol("X2C_SCOPE_COMMUNICATION_C", None)
        sym_SOURCE_FILE.setSourcePath("/templates/X2CScopeCommunication.c.ftl")
        sym_SOURCE_FILE.setOutputName("X2CScopeCommunication.c")
        sym_SOURCE_FILE.setDestPath("/X2CCode/X2CScope/src/")
        sym_SOURCE_FILE.setProjectPath("config/"+configName+"/X2CCode/X2CScope/")
        sym_SOURCE_FILE.setType("SOURCE")
        sym_SOURCE_FILE.setOverwrite(True)
        sym_SOURCE_FILE.setEnabled(True)
        sym_SOURCE_FILE.setMarkup(True)

        #Include Header Files
        sym_HEADER_FILE = self.component.createFileSymbol("X2C_SCOPE_H", None)
        sym_HEADER_FILE.setSourcePath("/library/inc/X2CScope.h")
        sym_HEADER_FILE.setOutputName("X2CScope.h")
        sym_HEADER_FILE.setDestPath("/X2CCode/X2CScope/inc/")
        sym_HEADER_FILE.setProjectPath("config/"+configName+"/X2CCode/X2CScope/")
        sym_HEADER_FILE.setType("HEADER")
        sym_HEADER_FILE.setOverwrite(True)
        sym_HEADER_FILE.setEnabled(True)
        sym_HEADER_FILE.setMarkup(True)

        sym_HEADER_FILE = self.component.createFileSymbol("X2C_SCOPE_COMMUNICATION_H", None)
        sym_HEADER_FILE.setSourcePath("/library/inc/X2CScopeCommunication.h")
        sym_HEADER_FILE.setOutputName("X2CScopeCommunication.h")
        sym_HEADER_FILE.setDestPath("/X2CCode/X2CScope/inc/")
        sym_HEADER_FILE.setProjectPath("config/"+configName+"/X2CCode/X2CScope/")
        sym_HEADER_FILE.setType("HEADER")
        sym_HEADER_FILE.setOverwrite(True)
        sym_HEADER_FILE.setEnabled(True)
        sym_HEADER_FILE.setMarkup(True)

        # Generate Initialization File
        sym_INIT_FILE = self.component.createFileSymbol("INITIALIZATION_X2C_SCOPE_C", None)
        sym_INIT_FILE.setType("STRING")
        sym_INIT_FILE.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE")
        sym_INIT_FILE.setSourcePath("templates/system/initialization.c.ftl")
        sym_INIT_FILE.setMarkup(True)

        sym_DEFINITION_FILE = self.component.createFileSymbol("X2C_SCOPE_SYS_DEF_HEADER", None)
        sym_DEFINITION_FILE.setType("STRING")
        sym_DEFINITION_FILE.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        sym_DEFINITION_FILE.setSourcePath("templates/system/definitions.h.ftl")
        sym_DEFINITION_FILE.setMarkup(True)

        #include directories
        sym_INCLUDE = self.component.createSettingSymbol("sym_INCLUDE", None)
        sym_INCLUDE.setCategory("C32")
        sym_INCLUDE.setKey("extra-include-directories")
        sym_INCLUDE.setValue("../src/config/"+ configName + "/X2CCode")
        sym_INCLUDE.setAppend(True, ";")

    def __call__(self):
        self.generateCode()



