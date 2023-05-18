import json
import requests
import textwrap
from utils.verifications.scrape import Scrape


def extractTwo(URL_book, status):
    #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
    
    wrapperI = textwrap.TextWrapper(width=45)
    wrapperII = textwrap.TextWrapper(width=35)

    r = requests.get(url=URL_book, headers=headers)
    if r.status_code == 200:
        book = json.loads(r.content)
        selector = book['volumeInfo']
        isbn10_selector = book['volumeInfo']['industryIdentifiers'][0]['identifier']
        isbn13_selector = book['volumeInfo']['industryIdentifiers'][1]['identifier']
        if 'subtitle' not in selector:
            title = book['volumeInfo']['title']
        else:
            title = book['volumeInfo']['title']," - ", book['volumeInfo']['subtitle']
            title = " ".join(title)
            title = wrapperI.fill(text=title)
            title = "".join(title)
        if 'authors' not in selector:
            authors = None
        else:
            authors = ", ".join(book['volumeInfo']['authors'])
            authors = wrapperII.fill(text=authors)
            authors = "".join(authors)
#            authors = ", ".join(book['volumeInfo']['authors'])
#            authors = book['volumeInfo']['authors']
        if 'publisher' not in selector:
            pub_company = None
        else:
            pub_company = book['volumeInfo']['publisher']
        if 'publishedDate' not in selector:
            pub_date = None
        else:
            pub_date = book['volumeInfo']['publishedDate']
        if isbn10_selector:
            isbn_10 = isbn10_selector
        else:
            isbn_10 = None
        if isbn13_selector:
            isbn_13 = isbn13_selector
        else:
            isbn_13 = None
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

    rating, price = Scrape(title)

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

    return item