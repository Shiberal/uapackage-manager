import winreg
def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(
        aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | flag)
    count_subkey = winreg.QueryInfoKey(aKey)[0]
    software_list = []
    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]
            try:
                software['path'] = winreg.QueryValueEx(
                asubkey, "InstallLocation")[0]
            except EnvironmentError:
                software['path'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue
    return software_list


def getReg():
    software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(
    winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0)
    return software_list



def getPathByName(appName):
    software_list = getReg()
    for software in software_list:
        if appName == software['name']:
            return software["path"]
    return "undefined"




def getRegByPath():
    software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(
    winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0)
    return software_list

