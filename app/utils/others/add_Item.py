# import json
from utils.others.get_MongoDB import getMongoDB
from utils.verifications.ack_Item import ackItem
from utils.verifications.auth_Path import authPath
from utils.verifications.extract_Two import extractTwo
from utils.verifications.path_User import pathUser
from utils.verifications.up_Item import upItem


def addItem(URL_book, collection, status, user_bookcase):

    item = extractTwo(URL_book, status)
    
    database = f"{user_bookcase}_books"
    directory, files = pathUser()
    conn_type = open(f"{directory}/.type_mongodb").read().strip()
    user, pwd, addr = authPath(directory, files)
    MongoDB = getMongoDB(conn_type, user, pwd, addr, database)
    collection = MongoDB[collection]
    ack_item = ackItem(
        item["título"], 
        item["isbn_10"], 
        item["isbn_13"], 
        collection
    )
    if ack_item == "No Exists":
        collection.insert_one(item)
        mongobook = collection.find_one(item)
        if mongobook:
            # mongobook['_id'] = str(mongobook['_id'])
            # mongobook = json.dumps(mongobook, ensure_ascii=False, indent=11)
            # with open("book.json", "w") as outfile:
            #     outfile.write(mongobook)
            return "item_Added"
    else:
        up_item = upItem(
            ack_item, item["categoria(s)"], 
            item["avaliação"], item["preço"], collection
        )
        if up_item == "No Update":
            return "prev_Registered"
        if up_item == "Update":
            return "up_Registered"
