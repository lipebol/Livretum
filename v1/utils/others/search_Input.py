import PySimpleGUI as sg
import requests
import json
from utils.window.icon import icon
from utils.window.screen import screen


def searchInput():
    #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
    
    sg.theme('DarkGrey11')

    x, y = 0.29282576866764276, 0.46875
    size_x, size_y, loc_x, loc_y = screen(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    search = sg.Text("Autor ou Assunto: ", font='Courier')
    searchItem = sg.InputText('', key="nameBook", size=(26), font='Courier', focus=True)
    data = n = "Exit"
    system_icon = icon()

    layout_searchInput = [
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Column([[search]])],
        [sg.Column([[searchItem]])],
        [sg.Text('')],
        [sg.Button("Pesquisar", font='Courier', bind_return_key=True)] # bind_return_key = Enter
    ]

    window_searchInput = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_searchInput,
        size=(size_x, size_y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(loc_x, loc_y)
    )

    while True:
        event, values = window_searchInput.read()
        if event == sg.WIN_CLOSED:
            return data, n
            break
        if event == "Pesquisar":
            nameBook = values["nameBook"]
            if nameBook != "":
                window_searchInput.Hide()
                try:
                    API = f"https://www.googleapis.com/books/v1/volumes?fields=items(selfLink,volumeInfo(title,subtitle,authors,imageLinks,industryIdentifiers))&q={nameBook}&maxResults=15&printType=books"
                    r = requests.get(url=API, headers=headers)
                except (requests.exceptions.ConnectionError):
                    return data, n
                else:
                    if r.status_code == 200:
                        data = json.loads(r.content)
                        n = 0
            
                return data, n