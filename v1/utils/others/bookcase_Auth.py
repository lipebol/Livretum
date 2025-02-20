from cpt.encr import encryptPath
from utils.others.input_Auth import inputAuth


def bookcaseAuth(directory):
    path = conn_type = "Repeat"
    while path == conn_type == "Repeat":
        path, conn_type = inputAuth()
    if path == conn_type == "Exit":
        return "Exit"
    else:
        encryptPath(directory, path, conn_type)
        return ""