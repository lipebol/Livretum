from utils.others.check_Search import checkSearch
from utils.others.others_Data import othersData
from utils.others.record_Book import recordBook
from utils.others.search_Input import searchInput


def cadasterBook(user_bookcase):
    data, n = searchInput()
    if data != n != "Exit":
        url_book = "No"
        while url_book == "No":
            url_book = checkSearch(data, n)
            n+=1
        if url_book != "Exit":
            collection = acquired = ""
            while collection == acquired == "":
                collection, acquired = othersData()
            if collection and acquired not in ("Exit"):
                if type(url_book) == dict:
                    url_book["Adquirido?"] = acquired
                    acquired = ""
                recordBook(url_book, collection, acquired, user_bookcase)
    
    return "Reload"
    