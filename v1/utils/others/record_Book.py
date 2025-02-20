import PySimpleGUI as sg
# import json
from utils.notifications.item_Added import itemAdded
from utils.notifications.prev_Registered import prevRegistered
from utils.notifications.up_Registered import upRegistered
from utils.others.add_Item import addItem
from utils.verifications.layout_recordBook import layoutrecordBook
from utils.window.icon import icon
from utils.window.screen import screen


# def queryNeo4j(query):
#     file = open('book.json')
#     docjson = json.load(file)
#     return query.run("""
#     WITH $docjson as data
#     UNWIND  data.título AS livro
#     MERGE (p:Autor {nome: data.autor})
#     MERGE (c: Coleção {nome: data.coleção})
#     MERGE (b:Livro {título: livro})
#     SET b.id_MongoDB = data._id, b.páginas = data.páginas, b.idioma = data.idioma, b.dt_pub = data.data_da_publicação
#     MERGE (e:Editora {nome: data.editora})
#     MERGE (p)-[:ESCREVEU]->(b)
#     MERGE (e)-[:PUBLICOU]->(b)
#     MERGE (b)-[:COLEÇÃO]->(c)
#     """, docjson = docjson
#     )


def recordBook(url_book, collection, acquired, user_bookcase):

    sg.theme('DarkGrey11')

    x, y = 0.43923865300146414, 0.8333333333333334
    size_x, size_y, loc_x, loc_y = screen(x, y)

    system_icon = icon()

    layout_recordBook = layoutrecordBook(url_book, collection, acquired)

    window_recordBook = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_recordBook,
        size=(size_x, size_y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(loc_x, loc_y)
    )

    while True:
        event, values = window_recordBook.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Cadastrar":
            window_recordBook.Hide()
            status = addItem(url_book, collection, acquired, user_bookcase)
            if status != "Exit":
                if status == "prev_Registered":
                    prevRegistered()
                if status == "up_Registered":
                    upRegistered()
                if status == "item_Added":
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
    #             confirmRegisteredBook()
    #             break