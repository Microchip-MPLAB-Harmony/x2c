######################  Harmony X2C Model  ######################
def loadModule():
    print("Load Module: Harmony X2C Model")

    #initiate X2C Scilab    
    # Symbol Name               Component        Component ID        Display Name    Display Path     File Path
    x2cModelcomponent = Module.CreateComponent("X2C Model", "X2C Model", "/X2C",  "config/x2c_model.py")
    x2cModelcomponent.setDisplayType("X2C Model")

    #Symbol Name                    Dependency ID     Dependency    Generic Required
    x2cModelcomponent.addDependency("x2cModelUartDependency", "UART",  False, True )
    
    # #Symbol Name                    Dependency ID     Dependency    Generic Required
    # x2cModelcomponent.addDependency("x2cModelTCPIPDependency", "TCP/IP",  True, False )    
    
    # #Symbol Name                    Dependency ID     Dependency    Generic Required
    # x2cModelcomponent.addDependency("x2cModelCANDependency", "CAN",  False, False )        

    # #Symbol Name                    Dependency ID     Dependency    Generic Required
    # x2cModelcomponent.addDependency("x2cModelUSBCDCDependency", "USB-CDC",  False, False )        
  