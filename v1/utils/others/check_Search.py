import PySimpleGUI as sg
from utils.verifications.extract_One import extractOne
from utils.verifications.has_Manually import hasManually
from utils.window.icon import icon
from utils.window.screen import screen


def checkSearch(data, n):
    
    sg.theme('DarkGrey11')

    x, y = 0.43923865300146414, 0.859375
    size_x, size_y, loc_x, loc_y = screen(x, y)
    try:
        url_book, title, authors, isbn_10, isbn_13, image = extractOne(data, n)
    except (IndexError, UnboundLocalError):
        manually = hasManually()
        return manually

    system_icon = icon()      
    logo = sg.Image(filename='app/src/images/Livretum.png')
    confirm_Book = sg.Text("É esse o livro?", font='Courier')
    bookImage = sg.Image(filename=image)
    textTitle = sg.Text(f"Nome: {title} ", font='Courier')
    textAuthors = sg.Text(f"Autor(es): {authors} ", font='Courier')
    textISBN10 = sg.Text(f"ISBN-10: {isbn_10}", font='Courier')
    textISBN13 = sg.Text(f"ISBN-13: {isbn_13} ", font='Courier')
    buttonYes = sg.Button("Sim", font='Courier')
    buttonNo = sg.Button("Não", font='Courier')
    
    layout_confirmSearch = [
        [sg.Text("")],
        [sg.Column([[logo]], justification='center')],
        [sg.Text("")],
        [sg.Column([[confirm_Book]], justification='center')],
        [sg.Column([[bookImage]], justification='center')],
        [sg.Text("")],
        [sg.Column([[textTitle]])],
        [sg.Column([[textAuthors]])],
        [sg.Column([[textISBN10]]), sg.Column([[textISBN13]])],
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
            manually = hasManually()
            return manually
        if event == "Não":
            window_confirmSearch.Hide()
            return "No"
            break
        if event == "Sim":
            window_confirmSearch.Hide()
            return url_book