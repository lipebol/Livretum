# apt install python3-tk

import PySimpleGUI as sg
# from utils.window.location import location
from cpt.gen import gen
from src.user_Bookcase import userBookcase
from src.my_Bookcase import myBookcase


def menuApp():
     
    sg.theme('DarkGrey11')

    x = 500
    y = 310
    
    # size_x, size_y = location(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    bookcase = sg.Button("Minha Estante", font='Courier 12')
    recommendation = sg.Button("Recomendações", font='Courier 12')
    version = sg.Text("v 0.2", font='Courier 8')
    gen()

    layout_menuApp = [ 
        [sg.Text('')],
        [sg.Column([[logo]], justification='center')],
        [sg.Text('')],
        [sg.Column([[bookcase]], justification='center')],
        [sg.Column([[recommendation]], justification='center')],
        [sg.Text('')],
        [sg.Column([[version]], justification='center')],
    ]
    
    window_menuApp = sg.Window(
        "Livretum",
        icon='app/src/images/icon_Livretum.png',
        layout=layout_menuApp,
        size=(x, y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9
        # location=(size_x, size_y)
    )

    while True:
        event, values = window_menuApp.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == "Minha Estante":
            window_menuApp.Hide()
            user_bookcase = userBookcase()
            if user_bookcase != "Exit":
                if user_bookcase != "Error":
                    result = "Reload"
                    while result == "Reload":
                        result = myBookcase(user_bookcase)
        window_menuApp.UnHide()