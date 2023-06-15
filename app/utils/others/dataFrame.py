import pandas as pd
from utils.verifications.conn_Database import connDatabase


def dataFrame(user_bookcase):

    MongoDB = connDatabase(user_bookcase)
    if MongoDB == "Error":
        return "Exit", "Exit"
    collections = MongoDB.list_collection_names()
    list_collection = []
    for i in collections:
        collection = MongoDB[i]
        for i in collection.find():
            i.pop("_id")
            list_collection.append(i)
        
    dataFrame = pd.DataFrame(list_collection)
    if dataFrame.columns.tolist() == []:
        cols = "No Records"
        values = "No Records"
    else:
        dataFrame[" id "] = range(1, len(dataFrame) + 1)
        dataFrame = dataFrame[[" id ", "título", "autor(es)", "Adquirido?"]]
        cols = dataFrame.columns.tolist()
        values = dataFrame.values.tolist()
    
    return cols, values