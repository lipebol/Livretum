import PySimpleGUI as sg
# from utils.window.location import location
from utils.verifications.path_User import pathUser
from utils.others.bookcase_Auth import bookcaseAuth
from utils.verifications.auth_Path import authPath
from utils.notifications.no_File import noFile
from utils.verifications.conn_Path import connPath


def userBookcase():

    sg.theme('DarkGrey11')

    x = 500
    y = 360

    # size_x, size_y = location(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    question_user_bookcase = sg.Text("Quem é o dono da estante?", font='Courier 14')
    user_bookcase = sg.InputText('', key="user_bookcase", size=(26), font='Courier 14')
    version = sg.Text("v 0.2", font='Courier 8')

    layout_userBookcase = [ 
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Column([[question_user_bookcase]])],
        [sg.Column([[user_bookcase]])],
        [sg.Text('')],
        [sg.Button("Enviar", font='Courier 12')],
        [sg.Text('')],
        [sg.Column([[version]])]
    ]
    
    window_userBookcase = sg.Window(
        "Livretum",
        icon='app/src/images/icon_Livretum.png',
        layout=layout_userBookcase,
        size=(x, y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c'
        # location=(size_x, size_y)
    )

    while True:
        event, values = window_userBookcase.read()
        if event == sg.WIN_CLOSED:
            return "Exit"
            break
        if event == "Enviar":
            user_bookcase = values["user_bookcase"]
            if user_bookcase != "":
                directory, files = pathUser()
                window_userBookcase.Hide()
                if ".path" not in files:
                    path, conn_type = bookcaseAuth(directory)
                    if path == None or conn_type == None:
                        return "Error"
                        break
                user, pwd, addr = authPath(directory, files)
                if user == None or pwd == None or addr == None:
                    noFile()
                    return "Error"
                    break
                result = connPath(directory, files, user_bookcase, user, pwd, addr)
                if result == "Exit":
                    return "Exit"
                if result == True:
                    return "Error"
                
                return user_bookcase