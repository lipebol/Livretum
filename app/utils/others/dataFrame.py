import pandas as pd
from utils.others.get_MongoDB import getMongoDB
from utils.verifications.auth_Path import authPath
from utils.verifications.path_User import pathUser


def dataFrame(user_bookcase):

    database = f"{user_bookcase}_books"
    directory, files = pathUser()
    conn_type = open(f"{directory}/.type_mongodb").read().strip()
    user, pwd, addr = authPath(directory, files)

    database = getMongoDB(conn_type, user, pwd, addr, database)
    collections = database.list_collection_names()
    list_collection = []
    for i in collections:
        collection = database[i]
        for i in collection.find():
            i.pop("_id")
            list_collection.append(i)
        
    dataFrame = pd.DataFrame(list_collection)
    if dataFrame.columns.tolist() == []:
        cols = "No Records"
        values = "No Records"
    else:
        dataFrame = dataFrame[["título", "autor(es)", "Adquirido?"]]
        cols = dataFrame.columns.tolist()
        values = dataFrame.values.tolist()
    
    return cols, values