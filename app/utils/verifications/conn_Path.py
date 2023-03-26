from utils.others.conn_MongoDB import connMongoDB
import os

def connPath(directory, files, user_bookcase, user, pwd, addr):
    result = user_bookcase
    if ".test" not in files:
        test, conn_error = connMongoDB(directory, user_bookcase, user, pwd, addr)
        result = conn_error
        if test == "Exit" or conn_error == "Exit":
            pass
        if test == True:
            test = "OK"
            with open(f"{directory}/.test", "w") as test_file:
                test_file.write(test)
            os.chmod(f"{directory}/.test", 0o400)
        if conn_error == True:
            os.remove(f"{directory}/.path")
            os.remove(f"{directory}/.type")
    return result