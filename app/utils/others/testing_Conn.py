import PySimpleGUI as sg
from utils.notifications.test_Conn import testConn
from utils.others.get_MongoDB import getMongoDB
from utils.verifications.layout_Conn import layout_Conn
from utils.window.icon import icon
from utils.window.screen import screen


def testingConn(directory, user_bookcase, user, pwd, addr):

    sg.theme('DarkGrey11')

    x, y = 0.3074670571010249, 0.625
    size_x, size_y, loc_x, loc_y = screen(x, y)

    MongoDB_logo = sg.Image(filename='app/src/images/MongoDB_logo.png')
    len_pwd = "*" * len(pwd)
    database = f"{user_bookcase}_books"
    testMongoDB = sg.Button("Conectar", font='Courier')
    system_icon = icon()
    conn_type, layout_testingConn = layout_Conn(
        directory, MongoDB_logo, user, len_pwd, addr, database, testMongoDB
    )

    window_testingConn = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_testingConn,
        size=(size_x, size_y),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        location=(loc_x, loc_y)
    )

    while True:
        event, values = window_testingConn.read()
        if event == sg.WIN_CLOSED:
            return "Exit"
            break
        if event == "Conectar":
            window_testingConn.Hide()
            connection = getMongoDB(conn_type, user, pwd, addr)
            if connection != "Error":
                testConn()
                return "OK"
                break
            else:
                return connection
                break
                