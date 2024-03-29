from utils.others.check_Search import checkSearch
from utils.others.others_Data import othersData
from utils.others.record_Book import recordBook
from utils.others.search_Input import searchInput

def cadasterBook(user_bookcase):
    data, n, headers = searchInput()
    URL_book = "Não"
    if data != n != headers != "Exit":
        while URL_book == "Não": 
            URL_book = checkSearch(data, n, headers)
            n+=1
        if URL_book != None:
            collection = "Repeat"
            status = "Repeat"
            while collection == "Repeat" or status == "Repeat":
                collection, status = othersData()
            if collection != "Exit" or status != "Exit":
                result = recordBook(URL_book, collection, status, user_bookcase)
                return result