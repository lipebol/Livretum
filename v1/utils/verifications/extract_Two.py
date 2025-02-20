import json
import requests
import textwrap
from utils.verifications.scrape import Scrape


def extractTwo(url_book, acquired):
    #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
    
    wrapperI = textwrap.TextWrapper(width=45)
    wrapperII = textwrap.TextWrapper(width=35)

    r = requests.get(url=url_book, headers=headers)
    if r.status_code == 200:
        book = json.loads(r.content)
        selector = book['volumeInfo']
        isbn_selector = isbn10 = isbn13 = "Not Found"
        if 'industryIdentifiers' in selector:
            if selector['industryIdentifiers'][0]['type'] in ("ISBN_10", "ISBN_13"):
                isbn_selector = selector['industryIdentifiers']
        if 'subtitle' not in selector:
            title = book['volumeInfo']['title']
        else:
            title = book['volumeInfo']['title']," - ", book['volumeInfo']['subtitle']
            title = " ".join(title)
            title = wrapperI.fill(text=title)
        if 'authors' not in selector:
            authors = None
        else:
            authors = ", ".join(book['volumeInfo']['authors'])
            authors = wrapperII.fill(text=authors)
        if 'publisher' not in selector:
            pub_company = None
        else:
            pub_company = book['volumeInfo']['publisher']
        if 'publishedDate' not in selector:
            pub_date = None
        else:
            pub_date = book['volumeInfo']['publishedDate']
        if isbn_selector != "Not Found":
            i = 0
            while i < len(isbn_selector):
                if len(isbn_selector[i]['identifier']) == 10:
                    isbn10 = isbn_selector[i]['identifier']
                else:
                    isbn13 = isbn_selector[i]['identifier']
                i +=1
        if 'pageCount' not in selector:
            pages = None
        else:
            pages = book['volumeInfo']['pageCount']
        if 'categories' not in selector:
            categories = None
        else:
            categories = book['volumeInfo']['categories']
            if len(categories) != 1:
                categories = " / ".join(categories)
            categories = "".join(categories)
            categories = list(dict.fromkeys(categories.split(" / ")))
            if "General" in categories:
                categories.remove("General")

    store, url_purchase, rating, price = Scrape(title)

    item = {
        "categoria(s)": categories,
        "título": title,
        "autor(es)": authors,
        "editora": pub_company,
        "data_da_publicação": pub_date,
        "isbn_10": isbn10,
        "isbn_13": isbn13,
        "páginas": pages,
        "loja": store,
        "link": url_purchase,
        "avaliação": rating,
        "preço": price,
        "Adquirido?": acquired
    }

    return item