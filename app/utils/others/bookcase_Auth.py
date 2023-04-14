from utils.others.input_Auth import inputAuth
from cpt.encr import encryptPath


def bookcaseAuth(directory):
    path = "Repeat"
    conn_type = "Repeat"
    while path == "Repeat" or conn_type == "Repeat":
        path, conn_type = inputAuth()
    if path == "Exit" or conn_type == "Exit":
        return path, conn_type
    else:
        encryptPath(directory, path, conn_type)
        path = False
        conn_type = False
        return path, conn_type