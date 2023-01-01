import PySimpleGUI as sg
from files_app_GUI.inform_CollectionStatus import window_collectionStatus
from pymongo import MongoClient
import json

def testConnMongoDB():

    sg.theme('DarkGrey11')

    messagetestConnMongoDB = sg.Text("Conectado", font='Courier 14')
   
    layout_testConnMongoDB = [
        [sg.Text("")],
        [sg.Column([[messagetestConnMongoDB]])],
    ]

    window_testConnMongoDB = sg.Window("Conn-MongoDB",icon='files_app_GUI/images/j.png', 
    layout = layout_testConnMongoDB, size=(200,100), resizable = True, element_justification='c', 
    finalize=True)

    while True:
        event, values = window_testConnMongoDB.read()
        if event == sg.WIN_CLOSED:
            break

def inputConnMongoDB():

    sg.theme('DarkGrey11')
    window_collectionStatus.hide()

    MongoDB_logo = sg.Image(filename='files_app_GUI/images/MongoDB_logo.png')
    buttonTestMongoDB = sg.Button("Próximo", font='Courier 12')
   
    layout_inputConnMongoDB = [
        [sg.Text("")],
        [sg.Column([[MongoDB_logo]], justification='center')],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Text("Usuário:", font='Courier 14'), sg.InputText('', key="userMongoDB", size=(30), 
        font='Courier 14')],
        [sg.Text("")],
        [sg.Text("Senha:", font='Courier 14'), sg.InputText('', key="passMongoDB", size=(32), 
        font='Courier 14')],
        [sg.Text("")],
        [sg.Text("Host:", font='Courier 14'), sg.InputText('', key="hostMongoDB", size=(33), 
        font='Courier 14')],
        [sg.Text("")],
        [sg.Text("Database:", font='Courier 14'), sg.InputText('', key="databaseMongoDB", size=(29), 
        font='Courier 14')],
        [sg.Text("")],
        [sg.Button("Teste de Conexão", font='Courier 12'), 
        sg.Column([[buttonTestMongoDB]], justification='center')],
        [sg.Text("")],
    ]

    window_inputConnMongoDB = sg.Window("jBook(MongoDB)", icon='files_app_GUI/images/j.png', 
    layout = layout_inputConnMongoDB, size=(480,420), resizable = True, finalize=True)

    while True:
        event, values = window_inputConnMongoDB.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Próximo":
            userMongoDB = values["userMongoDB"]
            passMongoDB = values["passMongoDB"]
            hostMongoDB = values["hostMongoDB"]
            databaseMongoDB = values["databaseMongoDB"]
            break
        if event == "Teste de Conexão":
            userMongoDB = values["userMongoDB"]
            passMongoDB = values["passMongoDB"]
            hostMongoDB = values["hostMongoDB"]
            databaseMongoDB = values["databaseMongoDB"]
            CONNECTION_STRING = "mongodb://{}:{}@{}:27017".format(userMongoDB, passMongoDB, 
            hostMongoDB)
            connection = MongoClient(CONNECTION_STRING)
            verify = connection.server_info()
            if verify:
                testConnMongoDB()
    
    return window_inputConnMongoDB, userMongoDB, passMongoDB, hostMongoDB, databaseMongoDB

window_inputConnMongoDB, userMongoDB, passMongoDB, hostMongoDB, databaseMongoDB = inputConnMongoDB()