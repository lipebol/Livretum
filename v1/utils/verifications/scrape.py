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
    n = 0
    kindle = True
    ebook = soup.find_all("div", {"class": "wFMWsc JCsJK OSrXXb"})
    if len(ebook) > n:
            for i in ebook:
                if "Kindle" in ebook[n].get_text():
                    n += 1
    soup_retail = soup.find_all("div", {"class": "yuRUbf"})
    soup_book = soup.find_all("div", {"class": "fG8Fp uo4vr"})
    url_purchase = soup_retail[n].find("a")['href']
    store = url_purchase.split("/")[2].split(".")[1] + ".com"
    items = soup_book[n].get_text()
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
    
    return store, url_purchase, rating, price