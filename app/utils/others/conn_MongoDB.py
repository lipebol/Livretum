import PySimpleGUI as sg
from utils.notifications.conn_Error import connError
from utils.notifications.test_Conn import testConn
from utils.verifications.layout_Conn import layout_Conn
from utils.verifications.testing_Conn import testingConn
from utils.window.icon import icon
from utils.window.screen import screen


def connMongoDB(directory, user_bookcase, user, pwd, addr):

    sg.theme('DarkGrey11')

    x, y = 0.3074670571010249, 0.625
    size_x, size_y, loc_x, loc_y = screen(x, y)

    MongoDB_logo = sg.Image(filename='app/src/images/MongoDB_logo.png')
    len_pwd = "*" * len(pwd)
    database = f"{user_bookcase}_books"
    testMongoDB = sg.Button("Conectar", font='Courier')
    system_icon = icon()
    conn_type, layout_connMongoDB = layout_Conn(
        directory, MongoDB_logo, user, len_pwd, addr, database, testMongoDB
    )

    window_connMongoDB = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_connMongoDB,
        size=(size_x, size_y),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        location=(loc_x, loc_y)
    )

    while True:
        event, values = window_connMongoDB.read()
        if event == sg.WIN_CLOSED:
            test = "Exit"
            conn_error = "Exit"
            return test, conn_error
            break
        if event == "Conectar":
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
                