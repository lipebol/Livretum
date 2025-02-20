import PySimpleGUI as sg
from files_app.conn_MongoDB import window_inputConnMongoDB
from neo4j import GraphDatabase
import json

def testConnNeo4j():

    sg.theme('DarkGrey11')

    messagetestConnNeo4j = sg.Text("Conectado", font='Courier 14')
   
    layout_testConnNeo4j = [
        [sg.Text("")],
        [sg.Column([[messagetestConnNeo4j]])],
    ]

    window_testConnNeo4j = sg.Window(
        "Conn-Neo4j",
        icon='files_app/images/icon_Livretum.png',
        layout = layout_testConnNeo4j,
        size=(200, 100),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c'
    )

    while True:
        event, values = window_testConnNeo4j.read()
        if event == sg.WIN_CLOSED:
            break

def inputConnNeo4j():

    sg.theme('DarkGrey11')
    window_inputConnMongoDB.hide()

    Neo4j_logo = sg.Image(filename='files_app/images/Neo4j_logo.png')
    buttonTestNeo4j = sg.Button("Próximo", font='Courier 12')
   
    layout_inputConnNeo4j = [
        [sg.Text("")],
        [sg.Column([[Neo4j_logo]], justification='center')],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Text("Usuário:", font='Courier 14'), sg.InputText('', key="userNeo4j", size=(30), font='Courier 14')],
        [sg.Text("")],
        [sg.Text("Senha:", font='Courier 14'), sg.InputText('', key="passNeo4j", size=(32), font='Courier 14')],
        [sg.Text("")],
        [sg.Text("Host:", font='Courier 14'), sg.InputText('', key="hostNeo4j", size=(33), font='Courier 14')],
        [sg.Text("")],
        [sg.Button("Teste de Conexão", font='Courier 12'), 
        sg.Column([[buttonTestNeo4j]], justification='center')],
        [sg.Text("")],
    ]

    window_inputConnNeo4j = sg.Window(
        "Livretum",
        icon='files_app/images/icon_Livretum.png',
        layout = layout_inputConnNeo4j,
        size=(480, 420),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9
    )

    while True:
        event, values = window_inputConnNeo4j.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Próximo":
            userNeo4j = values["userNeo4j"]
            passNeo4j = values["passNeo4j"]
            hostNeo4j = values["hostNeo4j"]
            break
        if event == "Teste de Conexão":
            userNeo4j = values["userNeo4j"]
            passNeo4j = values["passNeo4j"]
            hostNeo4j = values["hostNeo4j"]
            CONNECTION_STRING = "neo4j://{}:7687".format(hostNeo4j)
            connection = GraphDatabase.driver(CONNECTION_STRING, auth=(userNeo4j, passNeo4j))
            verify = connection.verify_connectivity()
            if verify == None:
                testConnNeo4j()

    return window_inputConnNeo4j, userNeo4j, passNeo4j, hostNeo4j

window_inputConnNeo4j, userNeo4j, passNeo4j, hostNeo4j = inputConnNeo4j()