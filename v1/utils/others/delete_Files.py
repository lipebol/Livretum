import os


def deleteFiles(directory, files):
    if ".mongodb" in files:
        os.remove(f"{directory}/.mongodb")
    if ".type_mongodb" in files:
        os.remove(f"{directory}/.type_mongodb")
    if ".test_mongodb" in files:
        os.remove(f"{directory}/.test_mongodb")