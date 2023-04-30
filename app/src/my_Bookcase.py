import PySimpleGUI as sg
import os
from utils.others.cadaster_Book import cadasterBook
from utils.others.dataFrame import dataFrame
from utils.verifications.layout_myBookcase import layoutmyBookcase
from utils.window.icon import icon
from utils.window.screen import screen


def myBookcase(user_bookcase):

    sg.theme('DarkGrey11')

    x, y = 0.4538799414348463, 0.5989583333333334
    size_x, size_y, loc_x, loc_y = screen(x, y)
    
    logo = sg.Image(filename='app/src/images/Livretum.png')
    cols, values = dataFrame(user_bookcase)
    system_icon = icon()
    
    layout_myBookcase = layoutmyBookcase(logo, cols, values)
        
    window_myBookcase = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_myBookcase,
        size=(size_x, size_y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(loc_x, loc_y)
    )

    while True:
        event, values = window_myBookcase.read()
        if event == sg.WIN_CLOSED:
            return "Exit"
            break
        if event == "Novo Livro":
            window_myBookcase.Hide()
            cadasterBook(user_bookcase)
            directory = 'app/src/images/'
            files = os.listdir(directory)
            if "book.png" in files:
                os.remove('app/src/images/book.png')
            return "Reload"
            break

        