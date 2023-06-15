from utils.others.delete_Files import deleteFiles
from utils.others.get_MongoDB import getMongoDB
from utils.verifications.auth_Path import authPath
from utils.verifications.path_User import pathUser

def connDatabase(user_bookcase):
    database = f"{user_bookcase}_books"
    directory, files = pathUser()
    conn_type = open(f"{directory}/.type_mongodb").read().strip()
    user, pwd, addr = authPath()
    MongoDB = getMongoDB(conn_type, user, pwd, addr)
    if MongoDB != "Error":
        return MongoDB[database]
    else:
        deleteFiles(directory, files)
        return MongoDB