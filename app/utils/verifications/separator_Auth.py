from utils.notifications.file_Format import fileFormat

def separatorAuth(auth):
    if str.count(auth, ":") == 4:
        if str.count(auth, "::") == 2:
            if auth[0:2] != "::" and auth[-2:] != "::":
                separator = True
            else:
                fileFormat()
                separator = False
            
            return separator