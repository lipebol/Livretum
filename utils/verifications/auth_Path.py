from cryptography.fernet import Fernet
import os
from utils.notifications.no_File import noFile
from utils.others.conn_MongoDB import connMongoDB


def authPath(directory, files, user_bookcase):
    try:
        with open(f"{directory}/.ps.key", "rb") as ps:
            key = ps.read()
        with open(f"{directory}/.path", "rb") as encrypt_file:
            encrypted = encrypt_file.read()
        fernet = Fernet(key)
        auth_path = fernet.decrypt(encrypted).decode()
        auth = open(auth_path).read().strip().split("=")
    except FileNotFoundError:
        os.remove(f"{directory}/.path")
        os.remove(f"{directory}/.type")
        os.remove(f"{directory}/.test")
        user = None
        pwd = None
        addr = None
    else:
        user = auth[0]
        pwd = auth[1]
        addr = auth[2]
    if user == None or pwd == None or addr == None:
        noFile()
        result = None
        return result
    else:
        if ".test" not in files:
            connMongoDB(directory, user_bookcase, user, pwd, addr)