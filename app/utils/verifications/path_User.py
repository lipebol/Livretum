import os


def pathUser():
    
    directory = os.path.expanduser('~/.docs_Livretum/')
    files = os.listdir(directory)

    return directory, files