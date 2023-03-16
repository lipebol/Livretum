import PySimpleGUI as sg
from cryptography.fernet import Fernet

def encryptPath(directory, path, conn_type):
    with open(f"{directory}/.ps.key", "rb") as ps:
        key = ps.read()
    fernet = Fernet(key)
    path = path.encode()
    encrypted = fernet.encrypt(path)
    with open(f"{directory}/.path", "wb") as encrypt_file:
        encrypt_file.write(encrypted)
    with open(f"{directory}/.type", "w") as type_file:
        type_file.write(conn_type)