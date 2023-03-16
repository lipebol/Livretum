import pymongo
from utils.notifications.test_Conn import testConn


def testingConn(directory, conn_type, user, pwd, addr):
    if conn_type == "Local":
        CONNECTION_STRING = f"mongodb://{user}:{pwd}@{addr}:27017"
    if conn_type == "Atlas":
        CONNECTION_STRING = f"mongodb+srv://{user}:{pwd}@{addr}.mongodb.net/?retryWrites=true&w=majority"
    try:
        connection = pymongo.MongoClient(CONNECTION_STRING)
        verify = connection.server_info()
        if verify:
            test = "OK"
            with open(f"{directory}/.test", "w") as test_file:
                test_file.write(test)
            testConn()
    except pymongo.errors.ConfigurationError:
        print("Tente novamente!")