import PySimpleGUI as sg
from utils.verifications.layout_Conn import layout_Conn
from utils.verifications.testing_Conn import testingConn


def connMongoDB(directory, user_bookcase, user, pwd, addr):

    sg.theme('DarkGrey11')

    MongoDB_logo = sg.Image(filename='src/images/MongoDB_logo.png')
    len_pwd = "*" * len(pwd)
    database_user = f"{user_bookcase}_books"
    buttonMongoDB = sg.Button("OK", font='Courier 12')
    version = sg.Text("v 0.2", font='Courier 8') 
    conn_type, layout_connMongoDB = layout_Conn(
        directory, MongoDB_logo, user, len_pwd, addr, database_user, buttonMongoDB, version
    )

    window_connMongoDB = sg.Window(
        "Livretum",
        icon='src/images/icon_Livretum.png',
        layout = layout_connMongoDB,
        size=(420, 510),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        finalize=True
    )

    while True:
        event, values = window_connMongoDB.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Teste de Conexão":
            testingConn(directory, conn_type, user, pwd, addr)