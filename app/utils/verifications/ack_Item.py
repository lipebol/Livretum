

def ackItem(title, isbn_10, isbn_13, collection):
    
    title_item = {
        "título": title
    }

    isbn10_item = {
        "isbn_10": isbn_10
    }

    isbn13_item = {
        "isbn_13": isbn_13
    }
    
    ack = collection.find_one(title_item)
    if ack == None:
        ack = collection.find_one(isbn10_item)
        if ack == None:
            ack = collection.find_one(isbn13_item)
            if ack == None:
                return "No Exists"
            else:
                return ack
        else:
            return ack
    else:
        return ack