from utils.verifications.conn_Database import connDatabase

def idChanged(user_bookcase, item):

    MongoDB = connDatabase(user_bookcase)
    if MongoDB == "Error":
        return "Exit"
    collections = MongoDB.list_collection_names()
    for name in collections:
        for i in MongoDB[name].find():
            if i['título'] == item[1]:
                locate = {
                    '_id': i['_id']
                    }
                item = MongoDB[name].find_one(locate)
                if item['Adquirido?'] == 'Não':
                    up = {
                        "$set": {'Adquirido?': 'Sim'}
                    }
                if item['Adquirido?'] == 'Sim':
                    up = {
                        "$set": {'Adquirido?': 'Não'}
                    }
                upStatus = MongoDB[name].update_one(locate, up)
                if upStatus.modified_count == 1:
                    return "Done!"