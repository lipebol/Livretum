import os


def pathUser():
    
    directory = os.path.expanduser('~/.livretum/')
    files = os.listdir(directory)

    return directory, files