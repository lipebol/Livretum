import platform

def icon():
    system = platform.system()
    if system == "Linux":
        system_icon = 'app/src/images/icon_Livretum.png'
    if system == "Windows":
        system_icon = 'app/src/images/icon_Livretum.ico'
    
    return system_icon