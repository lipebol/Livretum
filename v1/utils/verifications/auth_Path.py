from cryptography.fernet import Fernet
from utils.notifications.no_File import noFile
from utils.others.delete_Files import deleteFiles
from utils.verifications.path_User import pathUser
from utils.verifications.separator_Auth import separatorAuth


def authPath():
    directory, files = pathUser() # necessário para atualizar os arquivos que estão no dir;
    try:
        with open(f"{directory}/.ps.key", "rb") as ps:
            key = ps.read()
        with open(f"{directory}/.mongodb", "rb") as encrypt_file:
            encrypted = encrypt_file.read()
        fernet = Fernet(key)
        auth_path = fernet.decrypt(encrypted).decode()
        auth = open(auth_path).read().strip()
        separator = separatorAuth(auth)
    except FileNotFoundError:
        deleteFiles(directory, files)
        noFile()
        user = pwd = addr = "Not Found Error"
    else:
        if separator == True:
            auth = auth.split("::")
            user = auth[0]
            pwd = auth[1]
            addr = auth[2]
        else:
            deleteFiles(directory, files)
            user = pwd = addr = "File Error"

    return user, pwd, addr
            

