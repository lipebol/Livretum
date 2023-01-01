from archives_app.confirm_Book import collection, item
from pymongo import MongoClient
import json

def inputConnMongoDB():
    print("\n[MongoDB] \n")
    userMongoDB = input("  Usuário: ")
    passMongoDB = input("  Senha: ")
    hostMongoDB = input("  Host: ")
    databaseMongoDB = input("  Database: ")

    return userMongoDB, passMongoDB, hostMongoDB, databaseMongoDB

def getMongoDB():
    userMongoDB, passMongoDB, hostMongoDB, databaseMongoDB = inputConnMongoDB()
    CONNECTION_STRING = "mongodb://{}:{}@{}:27017".format(userMongoDB, passMongoDB, hostMongoDB)
    connection = MongoClient(CONNECTION_STRING)

    return connection[databaseMongoDB]

def toRecordBook():
    global collection
    MongoDB = getMongoDB()
    collection = MongoDB[collection]
    confirm_item = collection.find_one(item)
    if confirm_item:
        print("\nLivro já cadastrado.\n")
        exit()
    else:
        collection.insert_one(item)
        mongobook = collection.find_one(item)
        if mongobook:
            mongobook['_id'] = str(mongobook['_id'])
        mongobook = json.dumps(mongobook, ensure_ascii=False, indent=10)
#    create_json = json.dumps(mongobook, ensure_ascii=False, indent=10)
        with open("book.json", "w") as outfile:
            outfile.write(mongobook)

    return print("\n Gravado com Sucesso!\n")
    
  


