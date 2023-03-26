import pymongo

def testingConn(conn_type, user, pwd, addr):
    if conn_type == "Local":
        CONNECTION_STRING = f"mongodb://{user}:{pwd}@{addr}:27017"
    if conn_type == "Atlas":
        CONNECTION_STRING = f"mongodb+srv://{user}:{pwd}@{addr}.mongodb.net/?retryWrites=true&w=majority"
    try:
        connection = pymongo.MongoClient(CONNECTION_STRING)
        verify = connection.server_info()
        if verify:
            test = True
            conn_error = False
            return test, conn_error
    except (pymongo.errors.ConfigurationError, pymongo.errors.ServerSelectionTimeoutError):
        test = False
        conn_error = True
        return test, conn_error