import PySimpleGUI as sg
from utils.window.location import location
from utils.verifications.layout_Conn import layout_Conn
from utils.verifications.testing_Conn import testingConn
from utils.notifications.test_Conn import testConn
from utils.notifications.conn_Error import connError


def connMongoDB(directory, user_bookcase, user, pwd, addr):

    sg.theme('DarkGrey11')

    x = 420
    y = 510

    size_x, size_y = location(x, y)

    MongoDB_logo = sg.Image(filename='app/src/images/MongoDB_logo.png')
    len_pwd = "*" * len(pwd)
    database = f"{user_bookcase}_books"
    testMongoDB = sg.Button("Teste de Conexão", font='Courier 12')
    version = sg.Text("v 0.2", font='Courier 8') 
    conn_type, layout_connMongoDB = layout_Conn(
        directory, MongoDB_logo, user, len_pwd, addr, database, testMongoDB, version
    )

    window_connMongoDB = sg.Window(
        "Livretum",
        icon='app/src/images/icon_Livretum.png',
        layout = layout_connMongoDB,
        size=(x, y),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        location=(size_x, size_y)
    )

    while True:
        event, values = window_connMongoDB.read()
        if event == sg.WIN_CLOSED:
            test = "Exit"
            conn_error = "Exit"
            return test, conn_error
            break
        if event == "Teste de Conexão":
            test, conn_error = testingConn(conn_type, user, pwd, addr)
            if test == True:
                window_connMongoDB.Hide()
                testConn()
                return test, conn_error
                break
            if conn_error == True:
                window_connMongoDB.Hide()
                connError()
                return test, conn_error
                break
                