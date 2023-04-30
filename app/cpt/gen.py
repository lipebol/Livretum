from cryptography.fernet import Fernet
import os

def gen():
    HOME = os.path.expanduser('~')
    dirdocs_Livretum = f"{HOME}/.livretum"
    if not os.path.isdir(dirdocs_Livretum):
        os.makedirs(dirdocs_Livretum)
    os.chmod(dirdocs_Livretum, 0o700)
    files = os.listdir(dirdocs_Livretum)
    if ".ps.key" not in files:
        gen = Fernet.generate_key()
        with open(f"{dirdocs_Livretum}/.ps.key", "wb") as ps:
            ps.write(gen)
        os.chmod(f"{dirdocs_Livretum}/.ps.key", 0o400)