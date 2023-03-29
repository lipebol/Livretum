import PySimpleGUI as sg
from utils.window.location import location
import requests
import json


def searchInput():
     #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
    
    sg.theme('DarkGrey11')

    x = 400
    y = 390

    size_x, size_y = location(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    search = sg.Text("Autor ou Assunto: ", font='Courier 14')
    searchItem = sg.InputText('', key="nameBook", size=(26), font='Courier 14')
    version = sg.Text("v 0.2", font='Courier 8')

    layout_searchInput = [
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Column([[search]])],
        [sg.Column([[searchItem]])],
        [sg.Text('')],
        [sg.Button("Pesquisar", font='Courier 12')],
        [sg.Text('')],
        [sg.Column([[version]])]
    ]

    window_searchInput = sg.Window(
        "Livretum",
        icon='app/src/images/icon_Livretum.png',
        layout = layout_searchInput,
        size=(x, y),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(size_x, size_y)
    )

    while True:
        event, values = window_searchInput.read()
        if event == sg.WIN_CLOSED:
            data = n = headers = "Exit"
            break
        if event == "Pesquisar":
            nameBook = values["nameBook"]
            API = f"https://www.googleapis.com/books/v1/volumes?fields=items(selfLink,volumeInfo(title,subtitle,authors,imageLinks))&q={nameBook}&maxResults=40&printType=books"
            r = requests.get(url=API, headers=headers)
            if r.status_code == 200:
                data = json.loads(r.content)
                n = 0
                window_searchInput.Hide()
                break
     
    return data, n, headers