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

#-------------------------------------------------------------------------------------------#
#                                     Imports                                               #
#-------------------------------------------------------------------------------------------#
import os.path
import xml.etree.ElementTree as ET

#-------------------------------------------------------------------------------------------#
#                                  Global variables                                         #
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
#                                  File inclusions                                          #
#-------------------------------------------------------------------------------------------#
execfile(Module.getPath() + "/config/general_functions.py"  )
execfile(Module.getPath() + "/config/code_generation.py"  )

#-------------------------------------------------------------------------------------------#
#                                      Classes                                              #
#-------------------------------------------------------------------------------------------#

class X2CScope_InstanceClass:
    def __init__(self, component):
        self.component = component
        self.functionMap = {}
        MCU = Variables.get("__PROCESSOR")
        if( ("SAME7" in MCU) or ("SAMV7" in MCU) or ("SAMS7" in MCU)):
            global global_BAUD_RATE_SYMBOL
            global_BAUD_RATE_SYMBOL = "BAUD_RATE"
            self.functionMap = {"TRANSMIT": {}, "RECEIVE": {}}

            modulePath = "/avr-tools-device-file/devices/device/peripherals/module@[name=\"UART\"]"
            moduleRoot = ATDF.getNode(modulePath).getChildren()

            for module in moduleRoot:
                moduleInstance = module.getAttribute("name")

                channelPath = modulePath + "/instance@[name=\"" + moduleInstance + "\"]/signals"
                channelRoot = ATDF.getNode(channelPath).getChildren()
             
                for channel in channelRoot:
                    if(channel.getAttribute("group") == "URXD"):
                        try:
                            self.functionMap["RECEIVE"][moduleInstance].append(channel.getAttribute("pad"))
                        except:
                            self.functionMap["RECEIVE"][moduleInstance] = [channel.getAttribute("pad")]
                            
                    elif(channel.getAttribute("group") == "UTXD"):
                        try:
                            self.functionMap["TRANSMIT"][moduleInstance].append(channel.getAttribute("pad"))
                        except:
                            self.functionMap["TRANSMIT"][moduleInstance] = [channel.getAttribute("pad")]

                      
        elif("PIC32MK" in MCU):
            global global_BAUD_RATE_SYMBOL
            global_BAUD_RATE_SYMBOL = "USART_BAUD_RATE"

            # Pin to quadrature decoder mapping       
            currentPath = Variables.get("__CSP_DIR") + "/peripheral/gpio_02467"
            deviceXmlPath = os.path.join(currentPath, "plugin/pin_xml/components/" + Variables.get("__PROCESSOR") + ".xml")
            deviceXmlTree = ET.parse(deviceXmlPath)
            deviceXmlRoot = deviceXmlTree.getroot()
            pinoutXmlName = deviceXmlRoot.get("pins")
            pinoutXmlPath = os.path.join(currentPath, "plugin/pin_xml/pins/" + pinoutXmlName + ".xml")
            pinoutXmlPath = os.path.normpath(pinoutXmlPath)

            familiesXmlName = deviceXmlRoot.get("families")
            familiesXmlPath = os.path.join(currentPath, "plugin/pin_xml/families/" + familiesXmlName + ".xml")
            familiesXmlPath = os.path.normpath(familiesXmlPath)

            pinFileContent = ET.fromstring((open(familiesXmlPath, "r")).read())

            self.functionMap = {"TRANSMIT": {}, "RECEIVE":{}}
            for group in pinFileContent.findall("groups/group"):
                for function in group.findall("function"):
                    if function.attrib["name"].startswith("U") and "TX" in function.attrib["name"]:
                        for pin in group.findall("pin"):
                            channel = self.numericFilter(function.attrib["name"])
                            unit = "UART" + channel
                            pad = self.stringReplace(pin.attrib["name"])

                            try:
                                self.functionMap["TRANSMIT"][unit].append( pad )
                            except:
                                self.functionMap["TRANSMIT"][unit] = list()  
                                self.functionMap["TRANSMIT"][unit] = [pad]
                     
                    if function.attrib["name"].startswith("U") and "RX" in function.attrib["name"]:
                        for pin in group.findall("pin"):
                            channel = self.numericFilter(function.attrib["name"])
                            unit = "UART" + channel
                            pad = self.stringReplace(pin.attrib["name"])

                            try:
                                self.functionMap["RECEIVE"][unit].append(pad)
                            except:
                                self.functionMap["RECEIVE"][unit] = list()  
                                self.functionMap["RECEIVE"][unit] = [pad]  
            
        elif(("PIC32CM" in MCU) or ("SAMD2" in MCU) or ("SAMC2" in MCU) or ("SAML2" in MCU)):
            global global_BAUD_RATE_SYMBOL
            global_BAUD_RATE_SYMBOL = "BAUD_RATE"
            self.functionMap = {"TRANSMIT": {}, "RECEIVE": {}}

            modulePath = "/avr-tools-device-file/devices/device/peripherals/module@[name=\"SERCOM\"]"
            moduleRoot = ATDF.getNode(modulePath).getChildren()

            for module in moduleRoot:
                moduleInstance = module.getAttribute("name")

                channelPath = modulePath + "/instance@[name=\"" + moduleInstance + "\"]/signals"
                channelRoot = ATDF.getNode(channelPath).getChildren()
             
                for channel in channelRoot:
                    if(channel.getAttribute("index") != "0"):
                        try:
                            self.functionMap["RECEIVE"][moduleInstance].append(channel.getAttribute("pad"))
                        except:
                            self.functionMap["RECEIVE"][moduleInstance] = [channel.getAttribute("pad")]
                            
                    elif(channel.getAttribute("index") != "1"):
                        try:
                            self.functionMap["TRANSMIT"][moduleInstance].append(channel.getAttribute("pad"))
                        except:
                            self.functionMap["TRANSMIT"][moduleInstance] = [channel.getAttribute("pad")]
                   
                   
        elif( ("SAMD5" in MCU) or ("SAME5" in MCU)):
            global global_BAUD_RATE_SYMBOL
            global_BAUD_RATE_SYMBOL = "BAUD_RATE"
            self.functionMap = {"TRANSMIT": {}, "RECEIVE": {}}

            modulePath = "/avr-tools-device-file/devices/device/peripherals/module@[name=\"SERCOM\"]"
            moduleRoot = ATDF.getNode(modulePath).getChildren()

            for module in moduleRoot:
                moduleInstance = module.getAttribute("name")

                channelPath = modulePath + "/instance@[name=\"" + moduleInstance + "\"]/signals"
                channelRoot = ATDF.getNode(channelPath).getChildren()
             
                for channel in channelRoot:
                    if(channel.getAttribute("index") != "0"):
                        try:
                            self.functionMap["RECEIVE"][moduleInstance].append(channel.getAttribute("pad"))
                        except:
                            self.functionMap["RECEIVE"][moduleInstance] = [channel.getAttribute("pad")]
                            
                    elif(channel.getAttribute("index") != "1"):
                        try:
                            self.functionMap["TRANSMIT"][moduleInstance].append(channel.getAttribute("pad"))
                        except:
                            self.functionMap["TRANSMIT"][moduleInstance] = [channel.getAttribute("pad")]     
            
        elif("PIC32MX" in MCU):
            global global_BAUD_RATE_SYMBOL
            global_BAUD_RATE_SYMBOL = "USART_BAUD_RATE"
           
        elif("PIC32MZ" in MCU):
            global global_BAUD_RATE_SYMBOL
            global_BAUD_RATE_SYMBOL = "USART_BAUD_RATE"

        elif("SAMRH707" in MCU):
            global global_BAUD_RATE_SYMBOL
            global_BAUD_RATE_SYMBOL = "BAUD_RATE"
            self.functionMap = {"TRANSMIT": {}, "RECEIVE": {}}

            modulePath = "/avr-tools-device-file/devices/device/peripherals/module@[name=\"FLEXCOM\"]"
            moduleRoot = ATDF.getNode(modulePath).getChildren()

            for module in moduleRoot:
                moduleInstance = module.getAttribute("name")

                channelPath = modulePath + "/instance@[name=\"" + moduleInstance + "\"]/signals"
                channelRoot = ATDF.getNode(channelPath).getChildren()
             
                for channel in channelRoot:
                    if(channel.getAttribute("index") != "0"):
                        try:
                            self.functionMap["RECEIVE"][moduleInstance].append(channel.getAttribute("pad"))
                        except:
                            self.functionMap["RECEIVE"][moduleInstance] = [channel.getAttribute("pad")]
                            
                    elif(channel.getAttribute("index") != "1"):
                        try:
                            self.functionMap["TRANSMIT"][moduleInstance].append(channel.getAttribute("pad"))
                        except:
                            self.functionMap["TRANSMIT"][moduleInstance] = [channel.getAttribute("pad")]     
        else:
            Log.writeInfoMessage("Device Not Supported by X2C Scope")
    
    def getLibraryName(self):
        return self.librayName

    def stringReplace( self, my_String ):
        my_String = my_String.replace("RP","R")
        return my_String

    def numericFilter( self, input_String ):
        numeric_filter = filter(str.isdigit, str(input_String))
        return "".join(numeric_filter)

    def createSymbols(self):
        supported_Peripherals = ["UART"]
        sym_PERIPHERAL = self.component.createComboSymbol("X2C_COMM_INT", None, supported_Peripherals)
        sym_PERIPHERAL.setLabel("Communication Interface")
        sym_PERIPHERAL.setDefaultValue("UART")

        if (self.functionMap):
            global sym_INSTANCE
            instanceList = sorted(self.functionMap["RECEIVE"].keys())
            sym_INSTANCE = self.component.createComboSymbol("X2C_COMM_INSTANCE", sym_PERIPHERAL, instanceList)
            sym_INSTANCE.setLabel("Peripheral")
            sym_INSTANCE.setDefaultValue(instanceList[0])
            sym_INSTANCE.setDependencies(self.changeInstance, ["X2C_COMM_INSTANCE"])
            sym_INSTANCE.setReadOnly(True)
            sym_INSTANCE.setVisible(False)
            
            # Transmission pin 
            global sym_TRANSMIT
            sym_TRANSMIT = mcFun_AdvancedComboSymbol("Transmit", "TRANSMIT", self.component)
            sym_TRANSMIT.createComboSymbol( sym_INSTANCE, sym_PERIPHERAL, self.functionMap["TRANSMIT"])
            sym_TRANSMIT.setVisible(False)
            sym_TRANSMIT.setDefaultValue(self.functionMap["TRANSMIT"][instanceList[0]][0])
            sym_TRANSMIT.setReadOnly(True)
            
            # Reception pin 
            global sym_RECEIVE
            sym_RECEIVE = mcFun_AdvancedComboSymbol("Receive", "RECEIVE", self.component)
            sym_RECEIVE.createComboSymbol( sym_INSTANCE, sym_PERIPHERAL, self.functionMap["RECEIVE"])
            sym_RECEIVE.setDefaultValue(self.functionMap["RECEIVE"][instanceList[0]][0])
            sym_RECEIVE.setReadOnly(True)
            sym_RECEIVE.setVisible(False)
       
        sym_BAUD_RATE = self.component.createIntegerSymbol("X2C_SCOPE_BAUD_RATE", sym_PERIPHERAL)
        sym_BAUD_RATE.setLabel("Baud Rate")
        sym_BAUD_RATE.setDefaultValue(115200)
        sym_BAUD_RATE.setDependencies(self.updatePeripheral, ["X2C_SCOPE_BAUD_RATE"])

        global global_SELECTED_INSTANCE         
        global_SELECTED_INSTANCE = self.component.createStringSymbol("X2C_SCOPE_UART_ID", None)
        global_SELECTED_INSTANCE.setVisible(False)

        sym_USED_PERIPHERAL = self.component.createStringSymbol("X2C_SCOPE_PERIPH_USED", None)
        sym_USED_PERIPHERAL.setValue(sym_INSTANCE.getValue())
        sym_USED_PERIPHERAL.setVisible(False)

    def setSymbolValues(self):
        information = Database.sendMessage("bsp", "X2CSCOPE_READ_DAM_INFORMATION", {})
        if ( None != information):
            sym_INSTANCE.setValue(information["TRANSMIT"]["FUNCTION"][0][0])
            sym_TRANSMIT.setValue(information["TRANSMIT"]["PAD"])
            sym_RECEIVE.setValue(information["RECEIVE"]["PAD"])

    def handleMessage(self, ID, information):
        if("BSP_DATA_MONITORING" == ID) and ( None != information):
            sym_INSTANCE.setValue(information["TRANSMIT"]["FUNCTION"][0][0])
            sym_TRANSMIT.setValue(information["TRANSMIT"]["PAD"])
            sym_RECEIVE.setValue(information["RECEIVE"]["PAD"])



    def changeInstance(self, symbol, event):
        # Disconnect existing peripheral instance

        # Connect new instance 

        pass

    
    def updatePeripheral(self, symbol, event):
        status = setDatabaseSymbol(symbol.getValue(), global_BAUD_RATE_SYMBOL, event["value"])
        
        if status == False:
            # Log error
            pass



    def onAttachmentConnected( self, source, target):
        pass

    def onAttachmentDisconnected( self, source, target):
        pass

    def __call__(self):
        self.createSymbols()
        self.setSymbolValues()

#-------------------------------------------------------------------------------------------#
#                                      Component                                            #
#-------------------------------------------------------------------------------------------#
"""
Description:
This function is used to set database symbols 
"""
def setDatabaseSymbol(nameSpace, ID, value):
    status = Database.setSymbolValue(nameSpace, ID, value)
    if status == False:
        # Log error
        pass

"""
Description:
This function is used to handle message
"""
def handleMessage(messageID, args):
    init_Component.handleMessage(messageID, args)

"""
Description:
This function performs the task when the X2CScope module is connected
"""
def onAttachmentConnected(source, target):

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    
    srcID = source["id"]
    targetID = target["id"]
    
    
    if (srcID == "x2cScopeUartDependency"):
        peripheralName = Database.getSymbolValue(remoteID, "USART_PLIB_API_PREFIX")
        localComponent.getSymbolByID("X2C_SCOPE_PERIPH_USED").setValue("UART")
        localComponent.getSymbolByID("X2C_SCOPE_PERIPH_USED").clearValue()
        localComponent.getSymbolByID("X2C_SCOPE_PERIPH_USED").setValue(peripheralName)

        setDatabaseSymbol(remoteID, "USART_INTERRUPT_MODE", False)
        setDatabaseSymbol(remoteID, global_BAUD_RATE_SYMBOL, localComponent.getSymbolByID("X2C_SCOPE_BAUD_RATE").getValue())
        global_SELECTED_INSTANCE.setValue(remoteID)

        
"""
Description:
This function performs the task when the X2CScope module is disconnected
"""
def onAttachmentDisconnected(source, target):
    
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    srcID = source["id"]
    targetID = target["id"]

    if (srcID == "x2cScopeUartDependency"):
        localComponent.getSymbolByID("X2C_SCOPE_PERIPH_USED").clearValue()
 
"""
Description:
This function instantiates the X2CScope module
"""
def instantiateComponent(component):
        
    global init_Component
    init_Component = X2CScope_InstanceClass(component)
    init_Component()
    
    global code_Generation
    code_Generation = X2CScope_CodeGenerationClass(component)
    code_Generation()
