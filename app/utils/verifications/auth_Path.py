from cryptography.fernet import Fernet
from utils.others.delete_Files import deleteFiles


def authPath(directory, files):
    try:
        with open(f"{directory}/.ps.key", "rb") as ps:
            key = ps.read()
        with open(f"{directory}/.mongodb", "rb") as encrypt_file:
            encrypted = encrypt_file.read()
        fernet = Fernet(key)
        auth_path = fernet.decrypt(encrypted).decode()
        auth = open(auth_path).read().strip()
    except FileNotFoundError:
        deleteFiles(directory, files)
        user = "Not Found Error"
        pwd = "Not Found Error"
        addr = "Not Found Error"
    else:
        i = str.count(auth, "::")
        if i != 2:
            deleteFiles(directory, files)
            user = "File Error"
            pwd = "File Error"
            addr = "File Error"
        else:
            auth = auth.split("::")
            user = auth[0]
            pwd = auth[1]
            addr = auth[2]

    return user, pwd, addr
            

