import PySimpleGUI as sg
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
    user_bookcase = sg.InputText('', key="user_bookcase", size=(20), font='Courier', focus=True)
    directory, files = pathUser()
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
                window_userBookcase.Hide()
                if ".mongodb" not in files:
                    bookcaseStatus = bookcaseAuth(directory)
                    if bookcaseStatus == "Exit":
                        return bookcaseStatus
                        break
                user, pwd, addr = authPath()
                if user != pwd != addr:
                    conn = connPath(user_bookcase, user, pwd, addr)
                    if conn in ("Exit", "Error"):
                        return conn
                        break
                    return user_bookcase
                    break
                else:
                    return "Error"
                    break