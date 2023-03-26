# from cryptography.fernet import Fernet
import os


def authPath(directory, files):
    try:
        # with open(f"{directory}/.ps.key", "rb") as ps:
        #     key = ps.read()
        # with open(f"{directory}/.path", "rb") as encrypt_file:
        #     encrypted = encrypt_file.read()
        # fernet = Fernet(key)
        # auth_path = fernet.decrypt(encrypted).decode()
        with open(f"{directory}/.path", "r") as path_file:
            auth_path = path_file.read()
        auth = open(auth_path).read().strip().split("=")
    except FileNotFoundError:
        if ".path" in files:
            os.remove(f"{directory}/.path")
        if ".type" in files:
            os.remove(f"{directory}/.type")
        if ".test" in files:    
            os.remove(f"{directory}/.test")
        user = None
        pwd = None
        addr = None
    else:
        user = auth[0]
        pwd = auth[1]
        addr = auth[2]

    return user, pwd, addr
            

