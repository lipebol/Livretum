import PySimpleGUI as sg
from cpt.gen import gen
from src.my_Bookcase import myBookcase
from src.user_Bookcase import userBookcase
from utils.notifications.no_Net import noNet
from utils.verifications.network import network
from utils.window.icon import icon
from utils.window.screen import screen


def menuApp():
    
    status_net = network()
    if status_net == 0:
        noNet()
        exit()
        
    sg.theme('DarkGrey11')

    x, y = 0.36603221083455345, 0.390625
    size_x, size_y, loc_x, loc_y = screen(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    bookcase = sg.Button("Minha Estante", font='Courier')
    recommendation = sg.Button("Recomendações", font='Courier', disabled=True)
    system_icon = icon()
    gen()
    
    layout_menuApp = [ 
        [sg.Text('')],
        [sg.Column([[logo]], justification='center')],
        [sg.Text('')],
        [sg.Column([[bookcase]], justification='center')],
        [sg.Column([[recommendation]], justification='center')],
        [sg.Text('')]
    ]
    
    window_menuApp = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_menuApp,
        size=(size_x, size_y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        location=(loc_x, loc_y)
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