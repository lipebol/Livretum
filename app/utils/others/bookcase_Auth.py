from utils.others.input_Auth import inputAuth
from cpt.encr import encryptPath


def bookcaseAuth(directory):
    path, conn_type = inputAuth()
    if path == None or conn_type == None:
        return path, conn_type
    else:
        encryptPath(directory, path, conn_type)
        path = False
        conn_type = False
        return path, conn_type