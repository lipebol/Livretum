import PySimpleGUI as sg
from utils.window.location import location
from utils.verifications.extract_One import extractOne


def checkSearch(data, n, headers):
    
    sg.theme('DarkGrey11')

    x = 600
    y = 620

    size_x, size_y = location(x, y)

    URL_book, title, authors = extractOne(data, n, headers)
            
    logo = sg.Image(filename='app/src/images/Livretum.png')
    confirm_Book = sg.Text("É esse o livro?", font='Courier 14')
    bookImage = sg.Image(filename='app/src/images/book.png')
    textTitle = sg.Text(f"Nome: {title} ", font='Courier 14')
    textAuthors = sg.Text(f"Autor(es): {authors} ", font='Courier 14')
    buttonYes = sg.Button("Sim", key="Sim", font='Courier 12')
    buttonNo = sg.Button("Não", key="Não", font='Courier 12')
    
    layout_confirmSearch = [
        [sg.Text("")],
        [sg.Column([[logo]], justification='center')],
        [sg.Text("")],
        [sg.Column([[confirm_Book]], justification='center')],
        [sg.Column([[bookImage]], justification='center')],
        [sg.Text("")],
        [sg.Column([[textTitle]])],
        [sg.Column([[textAuthors]])],
        [sg.Text("")],
        [sg.Column([[buttonYes]], justification='center'), sg.Column([[buttonNo]])],
        [sg.Text("")],
    ]

    window_confirmSearch = sg.Window(
        "Livretum",
        icon='app/src/images/icon_Livretum.png',
        layout = layout_confirmSearch, 
        size=(x, y),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        location=(size_x, size_y)
    )

    while True:
        event, values = window_confirmSearch.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Não":
            window_confirmSearch.Hide()
            return "Não"
            break
        if event == "Sim":
            window_confirmSearch.Hide()
            return URL_book
            break