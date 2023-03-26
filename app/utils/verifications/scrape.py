import requests
from bs4 import BeautifulSoup

def Scrape(title):
    headers = {
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
    }

    r = requests.get(
        "https://www.google.com/search", 
        headers = headers, 
        params = {
            "q": "amazon" + title
            }
    )	
    soup = BeautifulSoup(r.text, "lxml")
    soup_book = soup.find_all("div", {"class": "fG8Fp uo4vr"})
    items = soup_book[0].get_text()
    list_items = list(items.split(" · \u200e"))
    if "Avaliação" not in items:
        rating = None
        if "R$" not in items:
            price = None
        else:
            price = list_items[0].split("\xa0")
            price = f"{price[0]} {price[1]}"
    else:
        rating = list_items[0].split(": ")[1] + f" ({list_items[1]})"
        if "R$" not in items:
            price = None
        else:
            price = list_items[2].split("\xa0")
            price = f"{price[0]} {price[1]}"
    
    return rating, price

    ### Scrape Google Shopping ###
    # r = requests.get(
    #     "https://www.google.com/search",
    #     headers = headers,
    #     params = {
    #         "q": title,
    #         "tbm": "shop"
    #     }
    # )
    # soup = BeautifulSoup(r.text, "lxml")
    # soup_book = soup.find_all("a", {"class": "shntl sh-np__click-target"})
    # price = soup_book[0].find("b", {"class" : "translate-content"}).get_text().split("\xa0")
    # price = " ".join(price)
    # store = soup_book[0].find("span", {"class" : "E5ocAb"}).get_text()
    
    # return price, store