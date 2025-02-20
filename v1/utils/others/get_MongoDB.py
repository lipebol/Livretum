import pymongo
from utils.notifications.conn_Error import connError
from utils.notifications.file_Format import fileFormat


def getMongoDB(conn_type, user, pwd, addr):
    if conn_type == "Local":
        CONNECTION_STRING = f"mongodb://{user}:{pwd}@{addr}:27017"
    if conn_type == "Atlas":
        CONNECTION_STRING = f"mongodb+srv://{user}:{pwd}@{addr}.mongodb.net/?retryWrites=true&w=majority"
    try:
        connection = pymongo.MongoClient(CONNECTION_STRING)
        verify = connection.server_info()
        if verify:
            return connection
    except (ValueError):
        fileFormat()
        connection = "Error"
        return connection
    except (pymongo.errors.OperationFailure, pymongo.errors.ConfigurationError, pymongo.errors.ServerSelectionTimeoutError):
        connError()
        connection = "Error"
        return connection