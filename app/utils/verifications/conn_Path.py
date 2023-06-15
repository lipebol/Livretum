import os
from utils.others.delete_Files import deleteFiles
from utils.others.testing_Conn import testingConn
from utils.verifications.path_User import pathUser


def connPath(user_bookcase, user, pwd, addr):
    directory, files = pathUser() # necessário para atualizar os arquivos que estão no dir;
    if ".test_mongodb" not in files:
        conn = testingConn(directory, user_bookcase, user, pwd, addr)
        if conn == "OK":
            with open(f"{directory}/.test_mongodb", "w") as test_file:
                test_file.write(conn)
            os.chmod(f"{directory}/.test_mongodb", 0o400)
        if conn in ("Exit", "Error"):
            deleteFiles(directory, files)
        return conn