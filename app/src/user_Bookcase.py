import PySimpleGUI as sg
from utils.notifications.no_File import noFile
from utils.others.bookcase_Auth import bookcaseAuth
from utils.verifications.auth_Path import authPath
from utils.verifications.conn_Path import connPath
from utils.verifications.path_User import pathUser
from utils.window.icon import icon
from utils.window.screen import screen


def userBookcase():

    sg.theme('DarkGrey11')

    x, y = 0.36603221083455345, 0.46875
    size_x, size_y, loc_x, loc_y = screen(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    question_user_bookcase = sg.Text("Quem é o dono da estante?", font='Courier')
    user_bookcase = sg.InputText('', key="user_bookcase", size=(26), font='Courier', focus=True)
    system_icon = icon()

    layout_userBookcase = [ 
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Column([[question_user_bookcase]])],
        [sg.Column([[user_bookcase]])],
        [sg.Text('')],
        [sg.Button("Enviar", font='Courier', bind_return_key=True)]
    ]
    
    window_userBookcase = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_userBookcase,
        size=(size_x, size_y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(loc_x, loc_y)
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
                if ".mongodb" not in files:
                    path, conn_type = bookcaseAuth(directory)
                    if path == "Exit" or conn_type == "Exit":
                        return "Exit"
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