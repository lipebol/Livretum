import PySimpleGUI as sg
from cryptography.fernet import Fernet
from src.user_Bookcase import userBookcase
import os


def menuApp():
     
    sg.theme('DarkGrey11')

    
    logo = sg.Image(filename='src/images/Livretum.png')
    bookcase = sg.Button("Minha Estante", font='Courier 12')
    recommendation = sg.Button("Recomendações", font='Courier 12')
    version = sg.Text("v 0.2", font='Courier 8')

    layout_menuApp = [ 
        [sg.Text('')],
        [sg.Column([[logo]], justification='center')],
        [sg.Text('')],
        [sg.Column([[bookcase]], justification='center')],
        [sg.Column([[recommendation]], justification='center')],
        [sg.Text('')],
        [sg.Column([[version]], justification='center')],
    ]

    HOME = os.path.expanduser('~')
    dirdocs_Livretum = f'{HOME}/.docs_Livretum'
    if not os.path.isdir(dirdocs_Livretum):
        os.makedirs(dirdocs_Livretum)
    files = os.listdir(dirdocs_Livretum)
    if ".ps.key" not in files:
        gen = Fernet.generate_key()
        with open(f'{dirdocs_Livretum}/.ps.key', 'wb') as ps:
            ps.write(gen)
    
    window_menuApp = sg.Window(
        "Livretum",
        icon='src/images/icon_Livretum.png',
        layout=layout_menuApp,
        size=(500, 310),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
    )

    while True:
        event, values = window_menuApp.read()
        # if event == sg.WIN_CLOSED:
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == "Minha Estante":
            window_menuApp.Hide()
            userBookcase()
            window_menuApp.UnHide()