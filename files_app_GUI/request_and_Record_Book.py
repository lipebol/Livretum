import PySimpleGUI as sg
from pymongo import MongoClient
from neo4j import GraphDatabase
from files_app_GUI.search_API import headers
from files_app_GUI.confirm_Search import n, URL_book
from files_app_GUI.inform_CollectionStatus import collection, status
from files_app_GUI.conn_MongoDB import userMongoDB, passMongoDB, hostMongoDB, databaseMongoDB
from files_app_GUI.conn_Neo4j import userNeo4j, passNeo4j, hostNeo4j
from files_app_GUI.conn_Neo4j import window_inputConnNeo4j
from files_app_GUI.scrape import Scrape
import requests
import json
import textwrap
import os


def getMongoDB():
    CONNECTION_STRING = "mongodb://{}:{}@{}:27017".format(userMongoDB, passMongoDB, hostMongoDB)
    connection = MongoClient(CONNECTION_STRING)

    return connection[databaseMongoDB]

def confirmItemMongoDB():

    sg.theme('DarkGrey11')

    messageconfirmItemMongoDB = sg.Text("Livro já cadastrado.", font='Courier 14')
   
    layout_confirmItemMongoDB = [
        [sg.Text("")],
        [sg.Column([[messageconfirmItemMongoDB]])],
    ]

    window_confirmItemMongoDB = sg.Window("Não se lembra?",icon='files_app_GUI/images/j.png', 
    layout = layout_confirmItemMongoDB, size=(400,100), resizable = True, element_justification='c', 
    finalize=True)

    while True:
        event, values = window_confirmItemMongoDB.read()
        if event == sg.WIN_CLOSED:
            break

def queryNeo4j(query):
    file = open('book.json')
    docjson = json.load(file)
    return query.run("""
    WITH $docjson as data
    UNWIND  data.título AS livro
    MERGE (p:Autor {nome: data.autor})
    MERGE (c: Coleção {nome: data.coleção})
    MERGE (b:Livro {título: livro})
    SET b.id_MongoDB = data._id, b.páginas = data.páginas, b.idioma = data.idioma, b.dt_pub = data.data_da_publicação
    MERGE (e:Editora {nome: data.editora})
    MERGE (p)-[:ESCREVEU]->(b)
    MERGE (e)-[:PUBLICOU]->(b)
    MERGE (b)-[:COLEÇÃO]->(c)
    """, docjson = docjson
    )

def confirmRegisteredBook():

    sg.theme('DarkGrey11')

    messageconfirmRegisteredBook = sg.Text("Gravado com Sucesso.", font='Courier 14')
   
    layout_confirmRegisteredBook = [
        [sg.Text("")],
        [sg.Column([[messageconfirmRegisteredBook]])],
    ]

    window_confirmRegisteredBook = sg.Window("jBook", icon='files_app_GUI/images/j.png', 
    layout = layout_confirmRegisteredBook, size=(400,100), 
    resizable=True, element_justification='c', finalize=True)

    while True:
        event, values = window_confirmRegisteredBook.read()
        if event == sg.WIN_CLOSED:
            break

def requestAndRecordBook():
    global collection
    #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}

    sg.theme('DarkGrey11')
    window_inputConnNeo4j.hide()
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
            
    rating, price = Scrape(title)

    jBook = sg.Image(filename='files_app_GUI/images/jBook.png')
    confirm_data_book = sg.Text("Dados do Livro", font='Courier 14')

    layout_requestAndRecordBook = [
        [sg.Text("")],
        [sg.Column([[jBook]])],
        [sg.Text("")],
        [sg.Column([[confirm_data_book]])],
        [sg.Text("{} ".format(title), font='Courier 12')],
        [sg.Text("Avaliação: {} ".format(rating), font='Courier 12')],
        [sg.Text("Autor(es): {} ".format(authors), font='Courier 12')],
        [sg.Text("Editora: {} ".format(pub_company), font='Courier 12')],
        [sg.Text("Publicação: {} ".format(publication_date), font='Courier 12')],
        [sg.Text("ISBN-10: {} ".format(isbn_10), font='Courier 12')],
        [sg.Text("ISBN-13: {} ".format(isbn_13), font='Courier 12')],
        [sg.Text("Páginas: {} ".format(pages), font='Courier 12')],
        [sg.Text("Idioma: {} ".format(language), font='Courier 12')],
        [sg.Text("Coleção: {} ".format(collection), font='Courier 12')],
        [sg.Text("Adquirido?: {} ".format(status), font='Courier 12')],
        [sg.Text("Preço: {} ".format(price), font='Courier 12')],
        [sg.Text("")],
        [sg.Button("Cadastrar", font='Courier 12')],
        [sg.Text("")],
    ]

    window_requestAndRecordBook = sg.Window("jBook", icon='files_app_GUI/images/j.png',
    layout = layout_requestAndRecordBook, size=(600,620), resizable = True, element_justification='c',
    finalize=True)

    while True:
        event, values = window_requestAndRecordBook.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Cadastrar":
            item = {
            "coleção" : collection,
            "título": title,
            "autor": authors,
            "editora": pub_company,
            "data_da_publicação": publication_date,
            "isbn_10": isbn_10,
            "isbn_13": isbn_13,
            "páginas": pages,
            "idioma": language,
            "Adquirido?": status,
            "avaliação": rating,
            "preço": price,
            }
            MongoDB = getMongoDB()
            collection = MongoDB[collection]
            confirm_item = collection.find_one(item)
            if confirm_item:
                window_requestAndRecordBook.hide()
                confirmItemMongoDB()
                break
            else:
                collection.insert_one(item)
                mongobook = collection.find_one(item)
                if mongobook:
                    mongobook['_id'] = str(mongobook['_id'])
                mongobook = json.dumps(mongobook, ensure_ascii=False, indent=10)
                with open("book.json", "w") as outfile:
                    outfile.write(mongobook)
            CONNECTION_STRING = "neo4j://{}:7687".format(hostNeo4j)
            connection = GraphDatabase.driver(CONNECTION_STRING, auth=(userNeo4j, passNeo4j))
            with connection.session() as session:
                session.execute_write(queryNeo4j)
                session.close()
                window_requestAndRecordBook.hide()
                with open('book.json','w') as cnt:
                    pass
                os.remove('book.json')
                os.remove('files_app_GUI/images/book.jpeg')
                os.remove('files_app_GUI/images/book.png')
                confirmRegisteredBook()
                break
    
    return None