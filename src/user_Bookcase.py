import PySimpleGUI as sg
import os
from utils.verifications.bookcase_Auth import bookcaseAuth
from utils.verifications.auth_Path import authPath



def userBookcase():

    sg.theme('DarkGrey11')

    logo = sg.Image(filename='src/images/Livretum.png')
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
        icon='src/images/icon_Livretum.png',
        layout=layout_userBookcase,
        size=(500, 360),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c'
    )

    while True:
        event, values = window_userBookcase.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Enviar":
            directory = os.path.expanduser('~/.docs_Livretum/')
            user_bookcase = values["user_bookcase"]
            if user_bookcase != "":
                files = os.listdir(directory)
                window_userBookcase.Hide()
                if ".path" not in files:
                    path, conn_type = bookcaseAuth(directory)
                    if path == None or conn_type == None:
                        break
                result = authPath(directory, files, user_bookcase)
                if result == None:
                    window_userBookcase.UnHide()