from cryptography.fernet import Fernet
import os

def encryptPath(directory, path, conn_type):
    with open(f"{directory}/.ps.key", "rb") as ps:
        key = ps.read()
    fernet = Fernet(key)
    path = path.encode()
    encrypted = fernet.encrypt(path)
    with open(f"{directory}/.mongodb", "wb") as encrypt_file:
        encrypt_file.write(encrypted)
    os.chmod(f"{directory}/.mongodb", 0o400)
    with open(f"{directory}/.type_mongodb", "w") as type_file:
        type_file.write(conn_type)
    os.chmod(f"{directory}/.type_mongodb", 0o400)