import PySimpleGUI as sg
from archives_app_GUI.request_and_Record_Book import window_requestBook

def confirmRegisteredBook():

    sg.theme('DarkGrey11')
    window_requestBook.hide()

    messageconfirmRegisteredBook = sg.Text("Gravado com Sucesso.", font='Courier 14')
   
    layout_messageconfirmRegisteredBook = [
        [sg.Text("")],
        [sg.Column([[messageconfirmRegisteredBook]])],
    ]

    window_messageconfirmRegisteredBook = sg.Window("jBook", icon='archives_app_GUI/images/j.png', 
    layout = layout_messageconfirmRegisteredBook, size=(400,100), 
    resizable=True, element_justification='c', finalize=True)

    while True:
        event, values = window_messageconfirmRegisteredBook.read()
        if event == sg.WIN_CLOSED:
            break
    
    return window_messageconfirmRegisteredBook

window_messageconfirmRegisteredBook = confirmRegisteredBook()