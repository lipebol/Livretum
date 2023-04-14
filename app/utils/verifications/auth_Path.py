from cryptography.fernet import Fernet
import os


def authPath(directory, files):
    try:
        with open(f"{directory}/.ps.key", "rb") as ps:
            key = ps.read()
        with open(f"{directory}/.mongodb", "rb") as encrypt_file:
            encrypted = encrypt_file.read()
        fernet = Fernet(key)
        auth_path = fernet.decrypt(encrypted).decode()
        auth = open(auth_path).read().strip().split("=")
    except FileNotFoundError:
        if ".mongodb" in files:
            os.remove(f"{directory}/.mongodb")
        if ".type_mongodb" in files:
            os.remove(f"{directory}/.type_mongodb")
        if ".test_mongodb" in files:    
            os.remove(f"{directory}/.test_mongodb")
        user = None
        pwd = None
        addr = None
    else:
        user = auth[0]
        pwd = auth[1]
        addr = auth[2]

    return user, pwd, addr
            

