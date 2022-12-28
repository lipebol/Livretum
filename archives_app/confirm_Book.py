from archives_app.search_API import headers
from archives_app.confirm_Search import n, URL_book
import requests
import json

def requestBook():
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
            title = "".join(title)
        if 'authors' not in selector:
            authors = None
        else:
#            authors = ", ".join(book['volumeInfo']['authors'])
            authors = book['volumeInfo']['authors']
        if 'publisher' not in selector:
            pub_company = None
        else:
            pub_company = book['volumeInfo']['publisher']
        if 'publishedDate' not in selector:
            publication_date = None
        else:
            publication_date = book['volumeInfo']['publishedDate']
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
        if 'language' not in selector:
            language = None
        else:
            language = book['volumeInfo']['language']
    else:
        print(" Não consegui recuperar! Desculpe. \n")
        print(" [Finished]")
        exit()

    collection = input("\n   Coleção: ")
    status = input("   Adquirido? (S/N): ")
    
    print("\n   Título: ", title)
    print("   Autor(es): ", authors)
    print("   Editora: ", pub_company)
    print("   Publicação: ", publication_date)
    print("   ISBN-10: ", isbn_10)
    print("   ISBN-13: ", isbn_13)
    print("   Páginas: ", pages)
    print("   Idioma: ", language)

    confirm_data_book = input("\n Confirma os dados? (s/n): ")
    if confirm_data_book == "s":
        item = {
            "coleção": collection,
            "título" : title,
            "autor" : authors,
            "editora": pub_company,
            "data_da_publicação" : publication_date,
            "isbn_10" : isbn_10,
            "isbn_13" : isbn_13,
            "páginas" : pages,
            "idioma" : language,
            "Adquirido?": status
            }
    elif confirm_data_book == "n":
        print("\n [Finished]")
        exit()
    else:
        print("\n Opção Inválida. \n")
        print("\n [Finished]")
        exit()
    
    return collection, item

collection, item = requestBook()