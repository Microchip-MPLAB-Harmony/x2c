var myVariable = `
{
  
  "0": {
    "title": "X2CScope",
    "content": ". MPLAB® Harmony X2C Scope . Introduction . X2C-Scope is a virtual oscilloscope tool developed by Linz Center of Mechatronics which allows run-time debugging or monitoring of your embedded application in MPLAB X IDE. This tool allows you to “Watch” or “Plot” any global variable in your embedded application at run-time i.e. without halting your CPU. . Using MPLAB Harmony Configurator (MHC), X2CScope can be seamlessly and automatically integrated into any Harmony 3 application. X2C-Scope uses UART to communicate with the target MCU allowing you to watch / update / plot a global variable in real-time. . Getting Started with X2CScope . Installing X2CScope Plugin in MPLAB® X IDE | Adding X2CScope to your MPLAB® Harmony Application | . Legal . Please review the Software License Agreement (mplab_harmony_license.md and X2CScope_license.md prior to using MPLAB Harmony and X2CScope. It is the responsibility of the end-user to know and understand the software license agreement terms regarding the Microchip and third-party software that is provided in this installation. .",
    "url": "http://localhost:4000/x2c/x2c-scope/docs/readme.html",
    "relUrl": "/x2c-scope/docs/readme.html"
  }
  ,"1": {
    "title": "X2C Model",
    "content": ". MPLAB® Harmony X2C Model . Introduction . MPLAB Harmony X2C Model enables rapid prototyping or model based development of a real time control embedded application using Scilab/Xcos + X2C within MPLAB Harmony 3 Embedded Software Development Framework. This model based development tool follows a hybrid approach where MPLAB Harmony 3 is used to configure and manage the target MCU and its I/O peripherals whereas a Scilab/Xcos + X2C is a model based development environment which is used to develop and manage the control algorithm running on the target MCU. . X2C is an embedded library for model based development of control algorithms developed by Linz Center of Mechatronics. For more information on X2C, please visit their website . Getting Started with X2C Model . Installing X2C Library | Create a “Blinky LED” demo using Scilab/Xcos + X2C in MPLAB Harmony 3 | .",
    "url": "http://localhost:4000/x2c/x2c-model/docs/readme.html",
    "relUrl": "/x2c-model/docs/readme.html"
  }
  ,"2": {
    "title": "Add X2CScope to your MPLAB® Harmony 3 Application",
    "content": "Add X2CScope to your MPLAB® Harmony 3 Application . This section provides a step by step guide to add X2CScope feature to ATSAMC21 based embedded application running on ATSAMC21 Motor Control Plugin Module + dsPICDEM™ MCLV-2 Development Board (Low Voltage) . Open ATSAMC21J18A based MPLAB Harmony Project to which X2CScope needs to be added. . | Open MPLAB® Harmony Configurator using Tools &gt; Plugin &gt; MPLAB® Harmony Configurator . | . . Just like in a real oscilloscope, the X2CScope also has a sampling rate at which the global variables are captured/updated. In this example, we will be using a fixed frequency timer event using TC1 to set the sampling rate. . | Add TC1 from Available Components &gt; Peripherals &gt; TC into the Project . | . . Configure the timer period of TC1 to be same as sampling rate of the X2CScope. Also enable the period match interrupt. In this example, the timer period is set to 50uS. . . | X2CScope plugin communicates with the target MCU via UART. Add the appropriate UART channel which is mapped on the board to communicate with the host PC running the MPLAB X IDE. On ATSAMC21 Motor Control Plugin Module + dsPICDEM™ MCLV-2 Development Board (Low Voltage) hardware setup, SERCOM3 can be configured as a UART channel which can communicate with the host PC. . | Add X2CScope component into the project and connect the UART port on X2CScope component to the UART port on SERCOM3 component. This configures X2CScope to user UART channel of SERCOM3 to communicate with X2CScope plugin on the host PC. Configure the recommended Baud Rate of 115200 bps using the X2CScope Component . . | Other than baud rate, following UART configurations are needed for establishing successful communication between target MCU and the host PC Map the UART TXD and RXD signals (this configuration requirement may vary from MCU to MCU).In this example, TXD is mapped onto PAD[0] and RXD is mapped onto PAD[1] | Set Transmit and Receive enable | Disable UART Interrupts (disabled by default upon connecting X2CScope to the UART peripheral) | Parity Mode - None (set by default) | Character Size - 8 (set by default) | Stop Bit - 1 (set by default) | Baud Rate - Recommended to set at 115200 (configured by default upon connecting X2CScope to UART peripheral) | . | Configure UART TX and RX pins using IO Pin Manager - MHC &gt; Tools &gt; Pin Configuration. In this example, PA22 is configured as SERCOM3_PAD0 [mapped as TXD] and PA23 is configured as SERCOM3_PAD1[mapped as RXD] | . . Generate Code | . . Adding X2CScope APIs Open main.c | Add X2CScope_Communicate() function call within the while(1) loop in the main function. This API establishes communication between the target MCU and the X2CScope plugin on the host PC. . . | X2CScope_Update() API samples the desired global variables. In order to sample the variables at a fixed rate (sampling rate), this API needs to be executed at the same rate as desired sampling rate. Typically, a timer is used to generate accurately timed interrupts which executes this API. In this example, TC1 is used to generate the sampling events and hence the X2CScope_Update() API is added in TC1 Interrupt Service Routine . . | . | Enable symbol loading in MPLAB X guide Go to File &gt; Project Properties &gt; Loading &gt; Enable “Load symbols when programming or building for production (slows process)” | . | Clean Build the project . . | Program the project into the target MCU . . | . Running X2CScope . Launch X2CScope plugin : Tools &gt; Embedded &gt; X2CScope . . | Connecting X2CScope . Connection setup Select relevant MPLAB X Project | Set Baud Rate same as UART channel - 115200 (recommended) | Set Data bits - 8 | Set Parity - None | Select relevant COM Port | . | . . Project setup Set Scope Sample time to match timer period which executes X2CScope_Update() at a fixed rate | Set Watch Sample time | Click on “Set Values” | . | . . Establish Connection by connecting “Disconnect/Connect” Toggle button | . . Using Scope View | . . Add the desired global variable to the corresponding channel and click “Sample” | . . ![](/x2c/x2c-scope/docs/images/x2cscope_running.png) . Using Watch View Click on “Watch View” under “Data Views” tab. | Click on “+” button to add the global variables to be watched | . . | . | .",
    "url": "http://localhost:4000/x2c/x2c-scope/docs/readme_add_x2cScope_to_your_application.html",
    "relUrl": "/x2c-scope/docs/readme_add_x2cScope_to_your_application.html"
  }
  ,"3": {
    "title": "Create an X2C Model based "Bliky LED" demo in MPLAB® Harmony 3",
    "content": "Create an X2C Model based “Bliky LED” demo in MPLAB® Harmony 3 . This section provides a step by step guide to create an X2C Model based “Bliky LED” demo in MPLAB Harmony 3 running on ATSAME54 Motor Control Plugin Module + dsPICDEM™ MCLV-2 Development Board (Low Voltage) . Create and setup an X2C Model project in MPLAB Harmony 3 . Create ATSAME54P20A based MPLAB Harmony 3 Project Open MPLAB X IDE -&gt; File -&gt; New Project -&gt; “32-bit MPLAB Harmony Project” -&gt; Set Harmony 3 Path -&gt; Set Project Location, Folder Name and Project Name -&gt; Set Configuration Name -&gt; Select Target MCU - ATSAME54P20A | . &nbsp; . &nbsp; . &nbsp; . | Open MPLAB Harmony Configurator Go to Tools -&gt; Embedded -&gt; MPLAB Harmony Configurator -&gt; Set MPLAB Harmony 3 Path -&gt; Select the default Device Family and CMSIS Pack Paths | . &nbsp; . &nbsp; . &nbsp; . | Add X2C Model from the list of Available Components -&gt; X2C -&gt; X2C Model into the project and connect the UART port on X2C Model component to the UART port on SERCOM2 component. This allows run time update to the X2C Model using X2C Communicator via UART channel of SERCOM2. Configure the recommended Baud Rate of 115200 bps using the X2C Model Component and set the “Receive Pinout” to SERCOM PAD[1] &nbsp; . &nbsp; . &nbsp; . | The control algorithm developed using X2C model is executed at a fixed interval which can be configured using a timer (TC0). Add TC0 to the project from the list of Available components -&gt; Peripherals -&gt; TC -&gt; TC0 &nbsp; . &nbsp; . &nbsp; . | Configure the timer period of TC0 to match the rate of model execution. Also enable the period match interrupt. In this example, the timer period is set to 50uS. &nbsp; . &nbsp; . &nbsp; . | Configure I/O pins using Pin Configurator Configure PD09 and PD10 as digital input for button switch BTN_S2 and BTN_S3 &nbsp; . &nbsp; . &nbsp; . | Configure PB26 and PB27 as digital output for LED_D2 and LED_D17 respectively &nbsp; . &nbsp; . &nbsp; . | Configure PA12 and PA13 as SERCOM2 PAD0 and PAD1 respectively &nbsp; . &nbsp; . &nbsp; . | . | Generate Code &nbsp; . &nbsp; . &nbsp; . | . Establish communication between X2C Communicator and Target MCU . Open Scilab &nbsp; . &nbsp; . &nbsp; . | Navigate to the project directory in Scilab where the MPLAB Harmony 3 Project was saved - &lt;harmony 3 project path&gt; firmware src config&lt;config name&gt; X2CCode X2CModel &nbsp; . &nbsp; . &nbsp; . | Generate code to configure X2C Communicator communication Open basicModel.zcos | Click on “transform model and push to communicator” | Click on “Start Communicator” | Wait till you see “Model Set” in the log | Click on “Create Code” button | . &nbsp; . &nbsp; . &nbsp; . | Add X2C Communicator API calls to MPLAB Harmony 3 Project Add X2C_Communicate() API in while(1) loop in main.c | Add X2C_UpdateModel() API as a call back to TC0 period match interrupt | Start TC0 Timer | . &nbsp; . &nbsp; . &nbsp; . | Make and Program Device Main Project &nbsp; . &nbsp; . &nbsp; . | Verify X2C Communicator Communication Click on “Start Communicator” (if not already open) | Setup Serial Port | Click on “Connect to Target” | . &nbsp; . &nbsp; . &nbsp; . | . Generate Code for Blinky LED model in Scilab/Xcos + X2C . Save X2C_Blinky_LED.zcos at &lt;harmony 3 project path&gt; firmware src config&lt;config name&gt; X2CCode X2CModel | Close any open instances of X2C Communicator | Open X2C_Blinky_LED.zcos in Scilab | Click on “transform model and push to communicator” | Click on “Start Communicator” | Wait till you see “Model Set” in the log | Click on “Create Code” button | . &nbsp; . &nbsp; . &nbsp; . Update “readInports” and “writeOutports” function calls in MPLABX Project . Open “PortConfigX2C.c” from Source Files -&gt; config -&gt; -&gt; X2CCode -&gt; X2CModel | Update readInports() as shown below . void readInports(void) { /* TODO add linkage hardware-inputs -&gt; X2C inports here * Pass the peripheral values to model Inports * if (PORTA &amp; 1) { * x2cModel.inports.bInport = INT16_MAX; * }else { * x2cModel.inports.bInport = 0; * } */ if(BTN_S2_Get()) { x2cModel.inports.bBTN_S2 = 0; } else { x2cModel.inports.bBTN_S2 = 1; } } . | Update writeOutports() as shown below . void writeOutports(void) { /* TODO add linkage hardware-inputs -&gt; X2C inports here * Pass the peripheral values to model Inports * if (PORTA &amp; 1) { * x2cModel.inports.bInport = INT16_MAX; * }else { * x2cModel.inports.bInport = 0; * } */ if((*x2cModel.outports.bLED_D2)) { LED_D2_Set(); } else { LED_D2_Clear(); } if((*x2cModel.outports.bLED_D17)) { LED_D17_Set(); } else { LED_D17_Clear(); } } . . | . &nbsp; . &nbsp; . &nbsp; . Make and Program Device with MPLAB Harmony 3 project updated with Blinky LED model | . &nbsp; . &nbsp; . &nbsp; . Running the X2C_Blinky_LED demo . Observe LED D2 turn ON when button switch S2 is pressed. . | Live update LED D17’s blink rate using Scilab/Xcos + X2C . Ensure X2C Communicator is connected | Increase/Decrease Frequency input to Sin3Gen block to increase/decrease the LED D17’s blink rate at run time | . | .",
    "url": "http://localhost:4000/x2c/x2c-model/docs/readme_create_x2c_model_blinky_led.html",
    "relUrl": "/x2c-model/docs/readme_create_x2c_model_blinky_led.html"
  }
  ,"4": {
    "title": "Installing MPLAB Harmony X2C Remote Package",
    "content": "Installing MPLAB® Harmony X2C Remote Package . Pre-requisites . MPLAB X IDE v5.40 or above | XC32 v2.41 or above | Install MPLAB Harmony Configurator Plugin in MPLAB X | . Install/update the latest revision of MPLAB Harmony X2C Remote Package . Open MPLAB X IDE | Go to Tools &gt; Embedded &gt; MPLAB Harmony Content Manager (MHCM) | Set Harmony 3 Installation Path and Installation Source | Scroll through the list of remote packages in MPLAB Harmony Content Manager and Select “x2c” and click Download | If the required pre-requisite remote packages for “x2c” are not available, then MHCM would prompt you to download the pre-requisite remote packages - Select “OK” | Accept “all” licenses and click “Next” | If the required pre-requisite remote packages for “x2c” are not available, then MHCM would prompt you to download the pre-requisite remote packages - Select “OK” | .",
    "url": "http://localhost:4000/x2c/x2c-model/docs/readme_installing_mh_x2c.html",
    "relUrl": "/x2c-model/docs/readme_installing_mh_x2c.html"
  }
  ,"5": {
    "title": "Installing X2CScope plugin in MPLAB® X IDE",
    "content": "Installing X2CScope plugin in MPLAB® X IDE . X2CScope comes as an MPLAB® X plugin which can be installed using the Plugin Manager. . Open MPLAB® X IDE | Go to Tools &gt; Plugins &gt; Available Plugins | Select X2CScope plugin and click “Install” | . . Follow the subsequent installation instructions. | In order to complete the installation MPLAB® X IDE needs to be restarted | . .",
    "url": "http://localhost:4000/x2c/x2c-scope/docs/readme_installing_x2cScope.html",
    "relUrl": "/x2c-scope/docs/readme_installing_x2cScope.html"
  }
  ,"6": {
    "title": "Installing X2C Library",
    "content": "Installing X2C Library . Pre-requisites . MPLAB® X IDE v5.40 or above | XC32 v2.41 or above | MPLAB Harmony Configurator Plugin in MPLAB X | Scilab v5.5.2 | MPLAB Harmony X2C Remote Package | . Install X2C Library . Visit this link to download X2C v6.3 or above. . | Run the X2C Installer and follow the instructions . | At “Select Components” menu, select “Compact Installation with Microchip Support” and click “Next” . | Certain library files from X2C are required to be copied to your local MPLAB Harmony 3 X2C installation folder. X2C Installer can do this task, transparent to the user, as long as the user provides the local Harmony 3 installation path as shown below. This step would copy the required library files at &lt;harmony 3 directory&gt; x2c_installer_files. . | . NOTE: This is a important step which adds Scilab/Xcos + X2C model based development support in MPLAB Harmony 3 environment . . Follow the rest of the self explanatory installation instructions to complete the installation of X2C. | X2C Installer will also download and install the requisite version of Scilab/Xcos (if not already installed) | .",
    "url": "http://localhost:4000/x2c/x2c-model/docs/readme_installing_x2c_library.html",
    "relUrl": "/x2c-model/docs/readme_installing_x2c_library.html"
  }
  ,"7": {
    "title": "",
    "content": "IMPORTANT: READ CAREFULLY . MICROCHIP IS WILLING TO LICENSE THIS INTEGRATED SOFTWARE FRAMEWORK SOFTWARE AND ACCOMPANYING DOCUMENTATION OFFERED TO YOU ONLY ON THE CONDITION THAT YOU ACCEPT ALL OF THE FOLLOWING TERMS. TO ACCEPT THE TERMS OF THIS LICENSE, CLICK “I ACCEPT” AND PROCEED WITH THE DOWNLOAD OR INSTALL. IF YOU DO NOT ACCEPT THESE LICENSE TERMS, CLICK “I DO NOT ACCEPT,” AND DO NOT DOWNLOAD OR INSTALL THIS SOFTWARE. . NON-EXCLUSIVE SOFTWARE LICENSE AGREEMENT FOR MICROCHIP MPLAB HARMONY INTEGRATED SOFTWARE FRAMEWORK . This Nonexclusive Software License Agreement (“Agreement”) is between you, your heirs, agents, successors and assigns (“Licensee”) and Microchip Technology Incorporated, a Delaware corporation, with a principal place of business at 2355 W. Chandler Blvd., Chandler, AZ 85224-6199, and its subsidiary, Microchip Technology (Barbados) II Incorporated (collectively, “Microchip”) for Microchip’s MPLAB Harmony Integrated Software Framework (“Software”) and accompanying documentation (“Documentation”). The Software and Documentation are licensed under this Agreement and not sold. U.S. copyright laws and international copyright treaties, and other intellectual property laws and treaties protect the Software and Documentation. Microchip reserves all rights not expressly granted to Licensee in this Agreement. . License and Sublicense Grant. . (a) Definitions. As used this Agreement, the following terms shall have the meanings defined below: . (i) &quot;Licensee Products&quot; means Licensee products that use or incorporate Microchip Products. (ii) &quot;Microchip Product&quot; means Microchip 16-bit and 32-bit microcontrollers, digital signal controllers or other Microchip semiconductor products with PIC16 and PIC18 prefix and specifically excepting the CX870 and CY920, which are not covered under this Agreement, that use or implement the Software. (iii) &quot;Object Code&quot; means the Software computer programming code provided by Microchip that is in binary form (including related documentation, if any) and error corrections, improvements and updates to such code provided by Microchip in its sole discretion, if any. (iv) &quot;Source Code&quot; means the Software computer programming code provided by Microchip that may be printed out or displayed in human readable form (including related programmer comments and documentation, if any), and error corrections, improvements, updates, modifications and derivatives of such code developed by Microchip, Licensee or Third Party. (v) &quot;Third Party&quot; means Licensee&#39;s agents, representatives, consultants, clients, customers, or contract manufacturers. (vi) &quot;Third Party Products&quot; means Third Party products that use or incorporate Microchip Products. . (b) Software License Grant. Subject to the terms of this Agreement, Microchip grants strictly to Licensee a personal, worldwide, non-exclusive, non-transferable limited license to use, modify (except as limited by Section 1(f) below), copy and distribute the Software only when the Software is embedded on a Microchip Product that is integrated into Licensee Product or Third Party Product pursuant to Section 2(d) below. . Any portion of the Software (including derivatives or modifications thereof) may not be: . (i) embedded on a non-Microchip microcontroller or digital signal controller; (ii) distributed (in Source Code or Object Code), except as described in Section 2(d) below. . (c) Documentation License Grant. Subject to all of the terms and conditions of this Agreement, Microchip grants strictly to Licensee a perpetual, worldwide, non-exclusive license to use the Documentation in support of Licensee’s use of the Software. . (d) Sublicense Grants. Subject to terms of this Agreement, Licensee may grant a limited sublicense to a Third Party to use the Software as described below only if such Third Party expressly agrees to be bound by terms of confidentiality and limited use that are no broader in scope and duration than the confidentiality and limited use terms of this Agreement: . (i) Third Party may modify Source Code for Licensee, except as limited by Section 1(f) below. (ii) Third Party may program Software into Microchip Products for Licensee. (iii) Third Party may use Software to develop and/or manufacture Licensee Product. (iv) Third Party may use Software to develop and/or manufacture Third Party Products where either: (x) the sublicensed Software contains Source Code modified or otherwise optimized by Licensee for Third Party use; or (y) the sublicensed Software is programmed into Microchip Products by Licensee on behalf of such Third Party. (v) Third Party may use the Documentation in support of Third Party&#39;s authorized use of the Software in conformance with this Section 2(d). . (e) Audit. Authorized representatives of Microchip shall have the right to reasonably inspect Licensee’s premises and to audit Licensee’s records and inventory of Licensee Products, whether located on Licensee’s premises or elsewhere at any time, announced or unannounced, and in its sole and absolute discretion, in order to ensure Licensee’s adherence to the terms of this Agreement. . (f) License and Sublicense Limitation. This Section 1 does not grant Licensee or any Third Party the right to modify any dotstack™ Bluetooth® stack, profile, or iAP protocol included in the Software. . | Third Party Requirements. Licensee acknowledges that it is Licensee’s responsibility to comply with any third party license terms or requirements applicable to the use of such third party software, specifications, systems, or tools, including but not limited to SEGGER Microcontroller GmbH &amp; Co. KG’s rights in the emWin software and certain libraries included herein. Microchip is not responsible and will not be held responsible in any manner for Licensee’s failure to comply with such applicable terms or requirements. . | Open Source Components. Notwithstanding the license grants contained herein, Licensee acknowledges that certain components of the Software may be covered by so-called “open source” software licenses (“Open Source Components”). Open Source Components means any software licenses approved as open source licenses by the Open Source Initiative or any substantially similar licenses, including any license that, as a condition of distribution, requires Microchip to provide Licensee with certain notices and/or information related to such Open Source Components, or requires that the distributor make the software available in source code format. Microchip will use commercially reasonable efforts to identify such Open Source Components in a text file or “About Box” or in a file or files referenced thereby (and will include any associated license agreement, notices, and other related information therein), or the Open Source Components will contain or be accompanied by its own license agreement. To the extent required by the licenses covering Open Source Components, the terms of such licenses will apply in lieu of the terms of this Agreement, and Microchip hereby represents and warrants that the licenses granted to such Open Source Components will be no less broad than the license granted in Section 1(b). To the extent the terms of the licenses applicable to Open Source Components prohibit any of the restrictions in this Agreement with respect to such Open Source Components, such restrictions will not apply to such Open Source Components. . | Licensee’s Obligations. . (a) Licensee will ensure Third Party compliance with the terms of this Agreement. . (b) Licensee will not: (i) engage in unauthorized use, modification, disclosure or distribution of Software or Documentation, or its derivatives; (ii) use all or any portion of the Software, Documentation, or its derivatives except in conjunction with Microchip Products; or (iii) reverse engineer (by disassembly, decompilation or otherwise) Software or any portion thereof; or (iv) copy or reproduce all or any portion of Software, except as specifically allowed by this Agreement or expressly permitted by applicable law notwithstanding the foregoing limitations. . (c) Licensee must include Microchip’s copyright, trademark and other proprietary notices in all copies of the Software, Documentation, and its derivatives. Licensee may not remove or alter any Microchip copyright or other proprietary rights notice posted in any portion of the Software or Documentation. . (d) Licensee will defend, indemnify and hold Microchip and its subsidiaries harmless from and against any and all claims, costs, damages, expenses (including reasonable attorney’s fees), liabilities, and losses, including without limitation product liability claims, directly or indirectly arising from or related to: (i) the use, modification, disclosure or distribution of the Software, Documentation or any intellectual property rights related thereto; (ii) the use, sale, and distribution of Licensee Products or Third Party Products, and (iii) breach of this Agreement. THE FOREGOING STATES THE SOLE AND EXCLUSIVE LIABILITY OF THE PARTIES FOR INTELLECTUAL PROPERTY RIGHTS INFRINGEMENT. . | Confidentiality. . (a) Licensee agrees that the Software (including but not limited to the Source Code, Object Code and library files) and its derivatives, Documentation and underlying inventions, algorithms, know-how and ideas relating to the Software and the Documentation are proprietary information belonging to Microchip and its licensors (“Proprietary Information”). Except as expressly and unambiguously allowed herein, Licensee will hold in confidence and not use or disclose any Proprietary Information and shall similarly bind its employees and Third Party(ies) in writing. Proprietary Information shall not include information that: (i) is in or enters the public domain without breach of this Agreement and through no fault of the receiving party; (ii) the receiving party was legally in possession of prior to receiving it; (iii) the receiving party can demonstrate was developed by it independently and without use of or reference to the disclosing party’s Proprietary Information; or (iv) the receiving party receives from a third party without restriction on disclosure. If Licensee is required to disclose Proprietary Information by law, court order, or government agency, such disclosure shall not be deemed a breach of this Agreement provided that Licensee gives Microchip prompt notice of such requirement in order to allow Microchip to object or limit such disclosure, Licensee cooperates with Microchip to protect Proprietary Information, and Licensee complies with any protective order in place and discloses only the information required by process of law. . (b) Licensee agrees that the provisions of this Agreement regarding unauthorized use and nondisclosure of the Software, Documentation and related Proprietary Rights are necessary to protect the legitimate business interests of Microchip and its licensors and that monetary damages alone cannot adequately compensate Microchip or its licensors if such provisions are violated. Licensee, therefore, agrees that if Microchip alleges that Licensee or Third Party has breached or violated such provision then Microchip will have the right to petition for injunctive relief, without the requirement for the posting of a bond, in addition to all other remedies at law or in equity. . | Ownership of Proprietary Rights. . (a) Microchip and its licensors retain all right, title and interest in and to the Software and Documentation (“Proprietary Rights”) including, but not limited to: (i) patent, copyright, trade secret and other intellectual property rights in the Software, Documentation, and underlying technology; (ii) the Software as implemented in any device or system, all hardware and software implementations of the Software technology (expressly excluding Licensee and Third Party code developed and used in conformance with this Agreement solely to interface with the Software and Licensee Products and/or Third Party Products); and (iii) all modifications and derivative works thereof (by whomever produced). Further, modifications and derivative works shall be considered works made for hire with ownership vesting in Microchip on creation. To the extent such modifications and derivatives do not qualify as a “work for hire,” Licensee hereby irrevocably transfers, assigns and conveys the exclusive copyright thereof to Microchip, free and clear of any and all liens, claims or other encumbrances, to the fullest extent permitted by law. Licensee and Third Party use of such modifications and derivatives is limited to the license rights described in Section 1 above. . (b) Licensee shall have no right to sell, assign or otherwise transfer all or any portion of the Software, Documentation or any related intellectual property rights except as expressly set forth in this Agreement. . | Termination of Agreement. Without prejudice to any other rights, this Agreement terminates immediately, without notice by Microchip, upon a failure by License or Third Party to comply with any provision of this Agreement. Further, Microchip may also terminate this Agreement upon reasonable belief that Licensee or Third Party have failed to comply with this Agreement. Upon termination, Licensee and Third Party will immediately stop using the Software, Documentation, and derivatives thereof, and immediately destroy all such copies, remove Software from any of Licensee’s tangible media and from systems on which the Software exists, and stop using, disclosing, copying, or reproducing Software (even as may be permitted by this Agreement). Termination of this Agreement will not affect the right of any end user or consumer to use Licensee Products or Third Party Products provided that such products were purchased prior to the termination of this Agreement. . | Dangerous Applications. The Software is not fault-tolerant and is not designed, manufactured, or intended for use in hazardous environments requiring failsafe performance (“Dangerous Applications”). Dangerous Applications include the operation of nuclear facilities, aircraft navigation, aircraft communication systems, air traffic control, direct life support machines, weapons systems, or any environment or system in which the failure of the Software could lead directly or indirectly to death, personal injury, or severe physical or environmental damage. Microchip specifically disclaims (a) any express or implied warranty of fitness for use of the Software in Dangerous Applications; and (b) any and all liability for loss, damages and claims resulting from the use of the Software in Dangerous Applications. . | Warranties and Disclaimers. THE SOFTWARE AND DOCUMENTATION ARE PROVIDED “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE. MICROCHIP AND ITS LICENSORS ASSUME NO RESPONSIBILITY FOR THE ACCURACY, RELIABILITY OR APPLICATION OF THE SOFTWARE OR DOCUMENTATION. MICROCHIP AND ITS LICENSORS DO NOT WARRANT THAT THE SOFTWARE WILL MEET REQUIREMENTS OF LICENSEE OR THIRD PARTY, BE UNINTERRUPTED OR ERROR-FREE. MICROCHIP AND ITS LICENSORS HAVE NO OBLIGATION TO CORRECT ANY DEFECTS IN THE SOFTWARE. LICENSEE AND THIRD PARTY ASSUME THE ENTIRE RISK ARISING OUT OF USE OR PERFORMANCE OF THE SOFTWARE AND DOCUMENTATION PROVIDED UNDER THIS AGREEMENT. . | Limited Liability. IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR OTHER LEGAL OR EQUITABLE THEORY FOR ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES INCLUDING BUT NOT LIMITED TO INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES (INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS. The aggregate and cumulative liability of Microchip and its licensors for damages hereunder will in no event exceed $1000 or the amount Licensee paid Microchip for the Software and Documentation, whichever is greater. Licensee acknowledges that the foregoing limitations are reasonable and an essential part of this Agreement. . | General. . (a) Governing Law, Venue and Waiver of Trial by Jury. THIS AGREEMENT SHALL BE GOVERNED BY AND CONSTRUED UNDER THE LAWS OF THE STATE OF ARIZONA AND THE UNITED STATES WITHOUT REGARD TO CONFLICTS OF LAWS PROVISIONS. Licensee agrees that any disputes arising out of or related to this Agreement, Software or Documentation shall be brought in the courts of State of Arizona. The parties agree to waive their rights to a jury trial in actions relating to this Agreement. . (b) Attorneys’ Fees. If either Microchip or Licensee employs attorneys to enforce any rights arising out of or relating to this Agreement, the prevailing party shall be entitled to recover its reasonable attorneys’ fees, costs and other expenses. . (c) Entire Agreement. This Agreement shall constitute the entire agreement between the parties with respect to the subject matter hereof. It shall not be modified except by a written agreement signed by an authorized representative of Microchip. . (d) Severability. If any provision of this Agreement shall be held by a court of competent jurisdiction to be illegal, invalid or unenforceable, that provision shall be limited or eliminated to the minimum extent necessary so that this Agreement shall otherwise remain in full force and effect and enforceable. . (e) Waiver. No waiver of any breach of any provision of this Agreement shall constitute a waiver of any prior, concurrent or subsequent breach of the same or any other provisions hereof, and no waiver shall be effective unless made in writing and signed by an authorized representative of the waiving party. . (f) Export Regulation. Licensee agrees to comply with all export laws and restrictions and regulations of the Department of Commerce or other United States or foreign agency or authority. . (g) Survival. The indemnities, obligations of confidentiality, and limitations on liability described herein, and any right of action for breach of this Agreement prior to termination shall survive any termination of this Agreement. . (h) Assignment. Neither this Agreement nor any rights, licenses or obligations hereunder, may be assigned by Licensee without the prior written approval of Microchip except pursuant to a merger, sale of all assets of Licensee or other corporate reorganization, provided that assignee agrees in writing to be bound by the Agreement. . (i) Restricted Rights. Use, duplication or disclosure by the United States Government is subject to restrictions set forth in subparagraphs (a) through (d) of the Commercial Computer-Restricted Rights clause of FAR 52.227-19 when applicable, or in subparagraph (c)(1)(ii) of the Rights in Technical Data and Computer Software clause at DFARS 252.227-7013, and in similar clauses in the NASA FAR Supplement. Contractor/manufacturer is Microchip Technology Inc., 2355 W. Chandler Blvd., Chandler, AZ 85225-6199. . | If Licensee has any questions about this Agreement, please write to Microchip Technology Inc., 2355 W. Chandler Blvd., Chandler, AZ 85224-6199 USA, ATTN: Marketing. . Microchip MPLAB Harmony Integrated Software Framework. Copyright © 2015 Microchip Technology Inc. All rights reserved. . License Rev. 11/2015 . Copyright © 2015 Qualcomm Atheros, Inc. All Rights Reserved. . Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies. . THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE. .",
    "url": "http://localhost:4000/x2c/mplab_harmony_license.html",
    "relUrl": "/mplab_harmony_license.html"
  }
  ,"8": {
    "title": "",
    "content": ". Microchip MPLAB® Harmony 3 Release Notes . X2C Release v1.1.0 . New Features . This release enables support for model based development using Scilab/Xcos + X2C Library within MPLAB® Harmony 3 embedded software framework environment on following MCU families . SAM C2x, SAM D2x, SAMLx | SAM D5x, SAM E5x | SAM E7x, SAM V7x, SAM S7x | PIC32MK, PIC32MX, PIC32MZ | . Known Issues . The current known issues are as follows: . “Double” data type (double precision floating point) variables are not supported in “Watch View” of X2CScope v1.3.0 plug-in | . Development Tools . MPLAB® X IDE v5.40 | MPLAB® XC32 C/C++ Compiler v2.41 | X2C v6.3 / X2C v6.2.1969 or above (latest nightly build) | MPLAB® X IDE plug-ins: MPLAB® Harmony Configurator (MHC) v3.5.0 and above. | X2CScope v1.3.0 Plugin | . | . X2C Release v1.0.1 . New Features . This release fixes a broken link for X2CScope License in v1.0.0 . Known Issues . Same as v1.0.0 . Development Tools . Same as v1.0.0 . X2C Release v1.0.0 . New Features . This release enables X2CScope plugin support for MPLAB® Harmony 3 application on following MCU families . SAM C2x, SAM D2x, SAMLx | SAM D5x, SAM E5x | SAM E7x, SAM V7x, SAM S7x | PIC32MK, PIC32MX, PIC32MZ | . Known Issues . The current known issues are as follows: . “Double” data type (double precision floating point) variables are not supported in “Watch View” of X2CScope v1.3.0 plug-in | . Development Tools . MPLAB® X IDE v5.40 | MPLAB® XC32 C/C++ Compiler v2.41 | MPLAB® X IDE plug-ins: MPLAB® Harmony Configurator (MHC) v3.5.0 and above. | X2CScope v1.3.0 Plugin | . | .",
    "url": "http://localhost:4000/x2c/release_notes.html",
    "relUrl": "/release_notes.html"
  }
  ,"9": {
    "title": "",
    "content": "Copyright (c) 2013, Linz Center of Mechatronics GmbH (LCM) http://www.lcm.at/ . All rights reserved. . X2Cscope binary is licensed according to the BSD 3-clause license as follows: . Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. . * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. * Neither the name of the &quot;Linz Center of Mechatronics GmbH&quot; and &quot;LCM&quot; nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission. . | THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL “Linz Center of Mechatronics GmbH” BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. . | This binary is part of X2C. http://www.mechatronic-simulation.org/ . | .",
    "url": "http://localhost:4000/x2c/x2c_scope_license.html",
    "relUrl": "/x2c_scope_license.html"
  }
  ,"10": {
    "title": "MPLAB® Harmony X2C",
    "content": "MPLAB® Harmony 3 X2C . MPLAB® Harmony 3 is an extension of the MPLAB ecosystem for creating embedded firmware solutions for Microchip 32-bit SAM and PIC® microcontroller and microprocessor devices. Refer to the following links for more information. . Microchip 32-bit MCUs | Microchip 32-bit MPUs | Microchip MPLAB X IDE | Microchip MPLAB® Harmony | Microchip MPLAB® Harmony Pages | . This repository contains the MPLAB Harmony 3 X2C solutions which includes support for X2CScope and model based development using Scilab/Xcos + X2C Library. Refer to the following links for release notes, training materials, and interface reference information. . Release Notes | MPLAB® Harmony License | X2CScope License | Learn more about installing MPLAB Harmony X2C Remote Package | Learn more about X2CScope support in MPLAB Harmony | Learn more about X2C Model support in MPLAB Harmony | MPLAB® Harmony 3 X2C Wiki | . Contents Summary . Folder Description . x2c-scope/config | X2CScope module configuration file | . x2c-model/config | X2C Model module configuration file | . . . . . .",
    "url": "http://localhost:4000/x2c/",
    "relUrl": "/"
  }
  
}`;
var data_for_search

var repo_name = "x2c";
var doc_folder_name = "docs";
var localhost_path = "http://localhost:4000/";
var home_index_string = "MPLAB® Harmony X2C";

(function (jtd, undefined) {

// Event handling

jtd.addEvent = function(el, type, handler) {
  if (el.attachEvent) el.attachEvent('on'+type, handler); else el.addEventListener(type, handler);
}
jtd.removeEvent = function(el, type, handler) {
  if (el.detachEvent) el.detachEvent('on'+type, handler); else el.removeEventListener(type, handler);
}
jtd.onReady = function(ready) {
  // in case the document is already rendered
  if (document.readyState!='loading') ready();
  // modern browsers
  else if (document.addEventListener) document.addEventListener('DOMContentLoaded', ready);
  // IE <= 8
  else document.attachEvent('onreadystatechange', function(){
      if (document.readyState=='complete') ready();
  });
}

// Show/hide mobile menu

function initNav() {
  const mainNav = document.querySelector('.js-main-nav');
  const pageHeader = document.querySelector('.js-page-header');
  const navTrigger = document.querySelector('.js-main-nav-trigger');

  jtd.addEvent(navTrigger, 'click', function(e){
    e.preventDefault();
    var text = navTrigger.innerText;
    var textToggle = navTrigger.getAttribute('data-text-toggle');

    mainNav.classList.toggle('nav-open');
    pageHeader.classList.toggle('nav-open');
    navTrigger.classList.toggle('nav-open');
    navTrigger.innerText = textToggle;
    navTrigger.setAttribute('data-text-toggle', text);
    textToggle = text;
  })
}

// Site search

function initSearch() {

    data_for_search = JSON.parse(myVariable);
    lunr.tokenizer.separator = /[\s/]+/

    var index = lunr(function () {
        this.ref('id');
        this.field('title', { boost: 200 });
        this.field('content', { boost: 2 });
        this.field('url');
        this.metadataWhitelist = ['position']

        var location = document.location.pathname;
        var path = location.substring(0, location.lastIndexOf("/"));
        var directoryName = path.substring(path.lastIndexOf("/")+1);

        var cur_path_from_repo = path.substring(path.lastIndexOf(repo_name));

        // Decrement depth by 2 as HTML files are placed in repo_name/doc_folder_name
        var cur_depth_from_doc_folder = (cur_path_from_repo.split("/").length - 2);

        var rel_path_to_doc_folder = "";

        if (cur_depth_from_doc_folder == 0) {
            rel_path_to_doc_folder = "./"
        }
        else {
            for (var i = 0; i < cur_depth_from_doc_folder; i++)
            {
                rel_path_to_doc_folder = rel_path_to_doc_folder + "../"
            }
        }

        for (var i in data_for_search) {

            data_for_search[i].url = data_for_search[i].url.replace(localhost_path + repo_name, rel_path_to_doc_folder);

            if (data_for_search[i].title == home_index_string)
            {
                data_for_search[i].url = data_for_search[i].url + "index.html"
            }

            this.add({
                id: i,
                title: data_for_search[i].title,
                content: data_for_search[i].content,
                url: data_for_search[i].url
            });
        }
    });

    searchResults(index, data_for_search);

function searchResults(index, data) {
    var index = index;
    var docs = data;
    var searchInput = document.querySelector('.js-search-input');
    var searchResults = document.querySelector('.js-search-results');

    function hideResults() {
      searchResults.innerHTML = '';
      searchResults.classList.remove('active');
    }

    jtd.addEvent(searchInput, 'keydown', function(e){
      switch (e.keyCode) {
        case 38: // arrow up
          e.preventDefault();
          var active = document.querySelector('.search-result.active');
          if (active) {
            active.classList.remove('active');
            if (active.parentElement.previousSibling) {
              var previous = active.parentElement.previousSibling.querySelector('.search-result');
              previous.classList.add('active');
            }
          }
          return;
        case 40: // arrow down
          e.preventDefault();
          var active = document.querySelector('.search-result.active');
          if (active) {
            if (active.parentElement.nextSibling) {
              var next = active.parentElement.nextSibling.querySelector('.search-result');
              active.classList.remove('active');
              next.classList.add('active');
            }
          } else {
            var next = document.querySelector('.search-result');
            if (next) {
              next.classList.add('active');
            }
          }
          return;
        case 13: // enter
          e.preventDefault();
          var active = document.querySelector('.search-result.active');
          if (active) {
            active.click();
          } else {
            var first = document.querySelector('.search-result');
            if (first) {
              first.click();
            }
          }
          return;
      }
    });

    jtd.addEvent(searchInput, 'keyup', function(e){
      switch (e.keyCode) {
        case 27: // When esc key is pressed, hide the results and clear the field
          hideResults();
          searchInput.value = '';
          return;
        case 38: // arrow up
        case 40: // arrow down
        case 13: // enter
          e.preventDefault();
          return;
      }

      hideResults();

      var input = this.value;
      if (input === '') {
        return;
      }

      var results = index.query(function (query) {
        var tokens = lunr.tokenizer(input)
        query.term(tokens, {
          boost: 10
        });
        query.term(tokens, {
          wildcard: lunr.Query.wildcard.TRAILING
        });
      });

      if (results.length > 0) {
        searchResults.classList.add('active');
        var resultsList = document.createElement('ul');
        resultsList.classList.add('search-results-list');
        searchResults.appendChild(resultsList);

        for (var i in results) {
          var result = results[i];
          var doc = docs[result.ref];

          var resultsListItem = document.createElement('li');
          resultsListItem.classList.add('search-results-list-item');
          resultsList.appendChild(resultsListItem);

          var resultLink = document.createElement('a');
          resultLink.classList.add('search-result');
          resultLink.setAttribute('href', doc.url);
          resultsListItem.appendChild(resultLink);

          var resultTitle = document.createElement('div');
          resultTitle.classList.add('search-result-title');
          resultTitle.innerText = doc.title;
          resultLink.appendChild(resultTitle);

          var resultRelUrl = document.createElement('span');
          resultRelUrl.classList.add('search-result-rel-url');
          resultRelUrl.innerText = doc.relUrl;
          resultTitle.appendChild(resultRelUrl);

          var metadata = result.matchData.metadata;
          var contentFound = false;
          for (var j in metadata) {
            if (metadata[j].title) {
              var position = metadata[j].title.position[0];
              var start = position[0];
              var end = position[0] + position[1];
              resultTitle.innerHTML = doc.title.substring(0, start) + '<span class="search-result-highlight">' + doc.title.substring(start, end) + '</span>' + doc.title.substring(end, doc.title.length)+'<span class="search-result-rel-url">'+doc.relUrl+'</span>';

            } else if (metadata[j].content && !contentFound) {
              contentFound = true;

              var position = metadata[j].content.position[0];
              var start = position[0];
              var end = position[0] + position[1];
              var previewStart = start;
              var previewEnd = end;
              var ellipsesBefore = true;
              var ellipsesAfter = true;
              for (var k = 0; k < 3; k++) {
                var nextSpace = doc.content.lastIndexOf(' ', previewStart - 2);
                var nextDot = doc.content.lastIndexOf('.', previewStart - 2);
                if ((nextDot > 0) && (nextDot > nextSpace)) {
                  previewStart = nextDot + 1;
                  ellipsesBefore = false;
                  break;
                }
                if (nextSpace < 0) {
                  previewStart = 0;
                  ellipsesBefore = false;
                  break;
                }
                previewStart = nextSpace + 1;
              }
              for (var k = 0; k < 10; k++) {
                var nextSpace = doc.content.indexOf(' ', previewEnd + 1);
                var nextDot = doc.content.indexOf('.', previewEnd + 1);
                if ((nextDot > 0) && (nextDot < nextSpace)) {
                  previewEnd = nextDot;
                  ellipsesAfter = false;
                  break;
                }
                if (nextSpace < 0) {
                  previewEnd = doc.content.length;
                  ellipsesAfter = false;
                  break;
                }
                previewEnd = nextSpace;
              }
              var preview = doc.content.substring(previewStart, start);
              if (ellipsesBefore) {
                preview = '... ' + preview;
              }
              preview += '<span class="search-result-highlight">' + doc.content.substring(start, end) + '</span>';
              preview += doc.content.substring(end, previewEnd);
              if (ellipsesAfter) {
                preview += ' ...';
              }

              var resultPreview = document.createElement('div');
              resultPreview.classList.add('search-result-preview');
              resultPreview.innerHTML = preview;
              resultLink.appendChild(resultPreview);
            }
          }
        }
      }
    });

    jtd.addEvent(searchInput, 'blur', function(){
      setTimeout(function(){ hideResults() }, 300);
    });
  }
}

function pageFocus() {
  var mainContent = document.querySelector('.js-main-content');
  mainContent.focus();
}

// Document ready

jtd.onReady(function(){
  initNav();
  pageFocus();
  if (typeof lunr !== 'undefined') {
    initSearch();
  }
});

})(window.jtd = window.jtd || {});


