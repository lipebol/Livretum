import pymongo


def getMongoDB(conn_type, user, pwd, addr, database):
    if conn_type == "Local":
        CONNECTION_STRING = f"mongodb://{user}:{pwd}@{addr}:27017"
    if conn_type == "Atlas":
        CONNECTION_STRING = f"mongodb+srv://{user}:{pwd}@{addr}.mongodb.net/?retryWrites=true&w=majority"

    connection = pymongo.MongoClient(CONNECTION_STRING)

    return connection[database]