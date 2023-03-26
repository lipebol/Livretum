import PySimpleGUI as sg
# from utils.window.location import location
from utils.verifications.layout_recordBook import layoutrecordBook
from utils.others.add_Item import addItem
from utils.notifications.prev_Registered import prevRegistered
from utils.notifications.item_Added import itemAdded
# import json
# import os


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

def recordBook(URL_book, collection, status, user_bookcase):

    sg.theme('DarkGrey11')

    x = 600
    y = 640

    # size_x, size_y = location(x, y)

    layout_recordBook = layoutrecordBook(URL_book, collection, status)

    window_recordBook = sg.Window(
        "Livretum",
        icon='app/src/images/icon_Livretum.png',
        layout = layout_recordBook,
        size=(x, y),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c'
        # location=(size_x, size_y)
    )

    while True:
        event, values = window_recordBook.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Cadastrar":
            result = addItem(URL_book, collection, status, user_bookcase)
            window_recordBook.Hide()
            if result == "prev_Registered":
                prevRegistered()
                break
            if result == "item_Added":
                itemAdded()
                break
                
    #         CONNECTION_STRING = "neo4j://{}:7687".format(hostNeo4j)
    #         connection = GraphDatabase.driver(CONNECTION_STRING, auth=(userNeo4j, passNeo4j))
    #         with connection.session() as session:
    #             session.execute_write(queryNeo4j)
    #             session.close()
    #             window_requestAndRecordBook.hide()
    #             with open('book.json','w') as cnt:
    #                 pass
    #             os.remove('book.json')
    #             os.remove('files_app/images/book.jpeg')
    #             os.remove('files_app/images/book.png')
    #             confirmRegisteredBook()
    #             break