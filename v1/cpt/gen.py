from cryptography.fernet import Fernet
import os

def gen():
    HOME = os.path.expanduser('~')
    directory = f"{HOME}/.livretum/"
    if not os.path.isdir(directory):
        os.makedirs(directory)
        os.chmod(directory, 0o700)
        files = os.listdir(directory)
        if ".ps.key" not in files:
            gen = Fernet.generate_key()
            with open(f"{directory}/.ps.key", "wb") as ps:
                ps.write(gen)
            os.chmod(f"{directory}/.ps.key", 0o400)
            return False
    else:
        return True