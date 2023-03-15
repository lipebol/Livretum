import PySimpleGUI as sg
import os
from cryptography.fernet import Fernet
import pymongo
import json

def testConnMongoDB():

    sg.theme('DarkGrey11')

    messagetestConnMongoDB = sg.Text("Conectado", font='Courier 14')
   
    layout_testConnMongoDB = [
        [sg.Text("")],
        [sg.Column([[messagetestConnMongoDB]])],
    ]

    window_testConnMongoDB = sg.Window(
        "Conn-MongoDB",
        icon='files_app/images/icon_Livretum.png',
        layout = layout_testConnMongoDB,
        size=(200, 100),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
    )

    while True:
        event, values = window_testConnMongoDB.read()
        if event == sg.WIN_CLOSED:
            break

def inputConnMongoDB(directory, user_bookcase, user, pwd):

    sg.theme('DarkGrey11')
    # window_collectionStatus.hide()

    MongoDB_logo = sg.Image(filename='files_app/images/MongoDB_logo.png')
    len_pwd = "*" * len(pwd)
    database_user = f"{user_bookcase}_books"
    buttonTestMongoDB = sg.Button("OK", font='Courier 12')
    version = sg.Text("v 0.2", font='Courier 8') 
    conn_type = open(f"{directory}/.type").read().strip()
    if conn_type == "Local":
        layout_inputConnMongoDB = [
        [sg.Text('')],
        [sg.Column([[MongoDB_logo]], justification='center')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text(f"Usuário: {user}", font='Courier 14')],
        [sg.Text('')],
        [sg.Text(f"Senha: {len_pwd}", font='Courier 14')],
        [sg.Text('')],
        [sg.Text(f"Host: @", font='Courier 14'), sg.InputText('', key="hostMongoDB", size=(20), 
        font='Courier 14'), sg.Text(":27017", font='Courier 14')],
        [sg.Text('')],
        [sg.Text(f"Database: {database_user}", font='Courier 14')],
        [sg.Text('')],
        [sg.Button("Teste de Conexão", font='Courier 12'), 
        sg.Column([[buttonTestMongoDB]], justification='center')],
        [sg.Text('')],
        [sg.Column([[version]], justification="center")]
    ]
    if conn_type == "Atlas":
        layout_inputConnMongoDB = [
        [sg.Text('')],
        [sg.Column([[MongoDB_logo]], justification='center')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text(f"Usuário: {user}", font='Courier 14')],
        [sg.Text('')],
        [sg.Text(f"Senha: {len_pwd}", font='Courier 14')],
        [sg.Text('')],
        [sg.Text(f"Host: @", font='Courier 14'), sg.InputText('', key="hostMongoDB", size=(20), 
        font='Courier 14'), sg.Text(".mongodb.net/", font='Courier 14')],
        [sg.Text('')],
        [sg.Text(f"Database: {database_user}", font='Courier 14')],
        [sg.Text('')],
        [sg.Button("Teste de Conexão", font='Courier 12'), 
        sg.Column([[buttonTestMongoDB]], justification='center')],
        [sg.Text('')],
        [sg.Column([[version]], justification="center")]
    ]

    window_inputConnMongoDB = sg.Window(
        "Livretum",
        icon='files_app/images/icon_Livretum.png',
        layout = layout_inputConnMongoDB,
        size=(500, 510),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        finalize=True
    )

    while True:
        event, values = window_inputConnMongoDB.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Teste de Conexão":
            userMongoDB = user
            passMongoDB = pwd
            hostMongoDB = values["hostMongoDB"]
            databaseMongoDB = database_user
            if conn_type == "Local":
                CONNECTION_STRING = f"mongodb://{userMongoDB}:{passMongoDB}@{hostMongoDB}:27017"
            if conn_type == "Atlas":
                CONNECTION_STRING = f"mongodb+srv://{userMongoDB}:{passMongoDB}@{hostMongoDB}.mongodb.net/?retryWrites=true&w=majority"
            try:
                connection = pymongo.MongoClient(CONNECTION_STRING)
                verify = connection.server_info()
                if verify:
                    testConnMongoDB()
            except pymongo.errors.ConfigurationError:
                print("Tente novamente!")