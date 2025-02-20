# import json
import textwrap
from utils.verifications.ack_Item import ackItem
from utils.verifications.conn_Database import connDatabase
from utils.verifications.extract_Two import extractTwo
from utils.verifications.up_Item import upItem


def addItem(url_book, collection, acquired, user_bookcase):

    if type(url_book) != dict:
        item = extractTwo(url_book, acquired)
        item[" coleção "] = collection
    else:
        item = url_book
        wrapperI = textwrap.TextWrapper(width=45)
        wrapperII = textwrap.TextWrapper(width=35)
        item["título"] = wrapperI.fill(text=item["título"])
        item["autor(es)"] = wrapperII.fill(text=item["autor(es)"])
        item[" coleção "] = collection
    
    MongoDB = connDatabase(user_bookcase)
    if MongoDB == "Error":
        return "Exit"
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
            ack_item, item["categoria(s)"], item["loja"],
            item["link"], item["avaliação"], item["preço"], collection
        )
        if up_item == "No Update":
            return "prev_Registered"
        if up_item == "Update":
            return "up_Registered"
