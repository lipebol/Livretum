import PySimpleGUI as sg
from utils.verifications.extract_One import extractOne
from utils.window.icon import icon
from utils.window.screen import screen


def checkSearch(data, n, headers):
    
    sg.theme('DarkGrey11')

    x, y = 0.43923865300146414, 0.8072916666666666
    size_x, size_y, loc_x, loc_y = screen(x, y)

    URL_book, title, authors, image = extractOne(data, n, headers)
    system_icon = icon()
            
    logo = sg.Image(filename='app/src/images/Livretum.png')
    confirm_Book = sg.Text("É esse o livro?", font='Courier')
    bookImage = sg.Image(filename=image)
    textTitle = sg.Text(f"Nome: {title} ", font='Courier')
    textAuthors = sg.Text(f"Autor(es): {authors} ", font='Courier')
    buttonYes = sg.Button("Sim", key="Sim", font='Courier')
    buttonNo = sg.Button("Não", key="Não", font='Courier')
    
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
        icon=system_icon,
        layout=layout_confirmSearch, 
        size=(size_x, size_y),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        location=(loc_x, loc_y)
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