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

#-------------------------------------------------------------------------------------------#
#                                  Functions                                                #
#-------------------------------------------------------------------------------------------#

def numericFilter( input_String ):
    numeric_filter = filter(str.isdigit, str(input_String))
    return "".join(numeric_filter)

def stringReplace( my_String ):
    my_String = my_String.replace("RP","R")
    return my_String

def getDeviceInformation(MCU):
    functionMap = {}
    if( ("SAME7" in MCU) or ("SAMV7" in MCU) or ("SAMS7" in MCU)):
        global global_BAUD_RATE_SYMBOL
        global_BAUD_RATE_SYMBOL = "BAUD_RATE"
        functionMap = {"TRANSMIT": {}, "RECEIVE": {}}

        modulePath = "/avr-tools-device-file/devices/device/peripherals/module@[name=\"UART\"]"
        moduleRoot = ATDF.getNode(modulePath).getChildren()

        for module in moduleRoot:
            moduleInstance = module.getAttribute("name")

            channelPath = modulePath + "/instance@[name=\"" + moduleInstance + "\"]/signals"
            channelRoot = ATDF.getNode(channelPath).getChildren()

            for channel in channelRoot:
                if(channel.getAttribute("group") == "URXD"):
                    try:
                        functionMap["RECEIVE"][moduleInstance].append(channel.getAttribute("pad"))
                    except:
                        functionMap["RECEIVE"][moduleInstance] = [channel.getAttribute("pad")]

                elif(channel.getAttribute("group") == "UTXD"):
                    try:
                        functionMap["TRANSMIT"][moduleInstance].append(channel.getAttribute("pad"))
                    except:
                        functionMap["TRANSMIT"][moduleInstance] = [channel.getAttribute("pad")]


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

        functionMap = {"TRANSMIT": {}, "RECEIVE":{}}
        for group in pinFileContent.findall("groups/group"):
            for function in group.findall("function"):
                if function.attrib["name"].startswith("U") and "TX" in function.attrib["name"]:
                    for pin in group.findall("pin"):
                        channel = numericFilter(function.attrib["name"])
                        unit = "UART" + channel
                        pad = stringReplace(pin.attrib["name"])

                        try:
                            functionMap["TRANSMIT"][unit].append( pad )
                        except:
                            functionMap["TRANSMIT"][unit] = list()
                            functionMap["TRANSMIT"][unit] = [pad]

                if function.attrib["name"].startswith("U") and "RX" in function.attrib["name"]:
                    for pin in group.findall("pin"):
                        channel = numericFilter(function.attrib["name"])
                        unit = "UART" + channel
                        pad = stringReplace(pin.attrib["name"])

                        try:
                            functionMap["RECEIVE"][unit].append(pad)
                        except:
                            functionMap["RECEIVE"][unit] = list()
                            functionMap["RECEIVE"][unit] = [pad]

    elif(("PIC32CM" in MCU) or ("SAMD2" in MCU) or ("SAMC2" in MCU) or ("SAML2" in MCU)):
        global global_BAUD_RATE_SYMBOL
        global_BAUD_RATE_SYMBOL = "BAUD_RATE"
        functionMap = {"TRANSMIT": {}, "RECEIVE": {}}

        modulePath = "/avr-tools-device-file/devices/device/peripherals/module@[name=\"SERCOM\"]"
        moduleRoot = ATDF.getNode(modulePath).getChildren()

        for module in moduleRoot:
            moduleInstance = module.getAttribute("name")

            channelPath = modulePath + "/instance@[name=\"" + moduleInstance + "\"]/signals"
            channelRoot = ATDF.getNode(channelPath).getChildren()

            for channel in channelRoot:
                if(channel.getAttribute("index") != "0"):
                    try:
                        functionMap["RECEIVE"][moduleInstance].append(channel.getAttribute("pad"))
                    except:
                        functionMap["RECEIVE"][moduleInstance] = [channel.getAttribute("pad")]

                elif(channel.getAttribute("index") != "1"):
                    try:
                        functionMap["TRANSMIT"][moduleInstance].append(channel.getAttribute("pad"))
                    except:
                        functionMap["TRANSMIT"][moduleInstance] = [channel.getAttribute("pad")]

    elif( ("SAMD5" in MCU) or ("SAME5" in MCU)):
        global global_BAUD_RATE_SYMBOL
        global_BAUD_RATE_SYMBOL = "BAUD_RATE"
        functionMap = {"TRANSMIT": {}, "RECEIVE": {}}

        modulePath = "/avr-tools-device-file/devices/device/peripherals/module@[name=\"SERCOM\"]"
        moduleRoot = ATDF.getNode(modulePath).getChildren()

        for module in moduleRoot:
            moduleInstance = module.getAttribute("name")

            channelPath = modulePath + "/instance@[name=\"" + moduleInstance + "\"]/signals"
            channelRoot = ATDF.getNode(channelPath).getChildren()

            for channel in channelRoot:
                if(channel.getAttribute("index") != "0"):
                    try:
                        functionMap["RECEIVE"][moduleInstance].append(channel.getAttribute("pad"))
                    except:
                        functionMap["RECEIVE"][moduleInstance] = [channel.getAttribute("pad")]

                elif(channel.getAttribute("index") != "1"):
                    try:
                        functionMap["TRANSMIT"][moduleInstance].append(channel.getAttribute("pad"))
                    except:
                        functionMap["TRANSMIT"][moduleInstance] = [channel.getAttribute("pad")]

    elif("PIC32MX" in MCU):
        global global_BAUD_RATE_SYMBOL
        global_BAUD_RATE_SYMBOL = "USART_BAUD_RATE"

    elif("PIC32MZ" in MCU):
        global global_BAUD_RATE_SYMBOL
        global_BAUD_RATE_SYMBOL = "USART_BAUD_RATE"

    elif("SAMRH707" in MCU):
        global global_BAUD_RATE_SYMBOL
        global_BAUD_RATE_SYMBOL = "BAUD_RATE"
        functionMap = {"TRANSMIT": {}, "RECEIVE": {}}

        modulePath = "/avr-tools-device-file/devices/device/peripherals/module@[name=\"FLEXCOM\"]"
        moduleRoot = ATDF.getNode(modulePath).getChildren()

        for module in moduleRoot:
            moduleInstance = module.getAttribute("name")

            channelPath = modulePath + "/instance@[name=\"" + moduleInstance + "\"]/signals"
            channelRoot = ATDF.getNode(channelPath).getChildren()

            for channel in channelRoot:
                if(channel.getAttribute("index") != "0"):
                    try:
                        functionMap["RECEIVE"][moduleInstance].append(channel.getAttribute("pad"))
                    except:
                        functionMap["RECEIVE"][moduleInstance] = [channel.getAttribute("pad")]

                elif(channel.getAttribute("index") != "1"):
                    try:
                        functionMap["TRANSMIT"][moduleInstance].append(channel.getAttribute("pad"))
                    except:
                        functionMap["TRANSMIT"][moduleInstance] = [channel.getAttribute("pad")]
    else:
        Log.writeInfoMessage("Device Not Supported by X2C Scope")

    return functionMap