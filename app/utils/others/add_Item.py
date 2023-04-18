# import json
from utils.others.get_MongoDB import getMongoDB
from utils.verifications.auth_Path import authPath
from utils.verifications.extract_Two import extractTwo
from utils.verifications.path_User import pathUser


def addItem(URL_book, collection, status, user_bookcase):

    title, authors, pub_company, pub_date, isbn_10, isbn_13, pages, categories, rating, price = extractTwo(URL_book)

    item = {
        "categoria(s)": categories,
        "título": title,
        "autor(es)": authors,
        "editora": pub_company,
        "data_da_publicação": pub_date,
        "isbn_10": isbn_10,
        "isbn_13": isbn_13,
        "páginas": pages,
        "Adquirido?": status,
        "avaliação": rating,
        "preço": price,
    }

    database = f"{user_bookcase}_books"
    directory, files = pathUser()
    conn_type = open(f"{directory}/.type_mongodb").read().strip()
    user, pwd, addr = authPath(directory, files)
    MongoDB = getMongoDB(conn_type, user, pwd, addr, database)
    collection = MongoDB[collection]
    confirm_item = collection.find_one(item)
    if confirm_item:
        return "prev_Registered"
    else:
        collection.insert_one(item)
        mongobook = collection.find_one(item)
        if mongobook:
            # mongobook['_id'] = str(mongobook['_id'])
            # mongobook = json.dumps(mongobook, ensure_ascii=False, indent=11)
            # with open("book.json", "w") as outfile:
            #     outfile.write(mongobook)

            return "item_Added"
    
    
    