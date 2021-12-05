######################  Harmony X2C-Scope  ######################
def loadModule():
    print("Load Module: Harmony X2CScope")
    #initiate x2c scope
    # Symbol Name               Component        Component ID        Display Name    Display Path     File Path
    x2cScopecomponent = Module.CreateComponent("X2CScope", "X2CScope", "/X2C",  "/config/x2c_scope.py")
    x2cScopecomponent.setDisplayType("X2CScope Module")

    #Symbol Name                    Dependency ID     Dependency    Generic Required
    x2cScopecomponent.addDependency("x2cScopeUartDependency", "UART",  False, True )
    
    x2cScopecomponent.addCapability("x2cScope_Scope", "Data stream")
