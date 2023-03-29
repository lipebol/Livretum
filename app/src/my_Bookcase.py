import PySimpleGUI as sg
from utils.window.location import location
from utils.others.dataFrame import dataFrame
from utils.verifications.layout_myBookcase import layoutmyBookcase
from utils.others.cadaster_Book import cadasterBook


def myBookcase(user_bookcase):

    sg.theme('DarkGrey11')

    x = 620
    y = 460

    size_x, size_y = location(x, y)
    
    logo = sg.Image(filename='app/src/images/Livretum.png')
    cols, values = dataFrame(user_bookcase)
    layout_myBookcase = layoutmyBookcase(logo, cols, values)
        
    window_myBookcase = sg.Window(
        "Livretum",
        icon='app/src/images/icon_Livretum.png',
        layout = layout_myBookcase,
        size=(x, y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(size_x, size_y)
    )

    while True:
        event, values = window_myBookcase.read()
        if event == sg.WIN_CLOSED:
            return "Exit"
            break
        if event == "🔄":
            window_myBookcase.Hide()
            return "Reload"
            break
        if event == "Novo Livro":
            window_myBookcase.Hide()
            cadasterBook(user_bookcase)
            return "Reload"
            break

        