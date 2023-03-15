# apt install python3-tk

import PySimpleGUI as sg
import requests
import json


def searchInput():
#    global n, data
     #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
    
    sg.theme('DarkGrey11')

    logo = sg.Image(filename='files_app/images/Livretum.png')
    search = sg.Text("Autor ou Assunto: ", font='Courier 14')
    searchInput = sg.InputText('', key="nameBook", size=(26), font='Courier 14')

    layout_searchInput = [
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Column([[search]])],
        [sg.Column([[searchInput]])],
        [sg.Text('')],
        [sg.Button("Pesquisar", font='Courier 12')],
        [sg.Text('')],
    ]

    window_searchInput = sg.Window(
        "Livretum",
        icon='files_app/images/icon_Livretum.png',
        layout = layout_searchInput,
        size=(400, 360),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c'
    )

    while True:
        event, values = window_searchInput.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Pesquisar":
            nameBook = values["nameBook"]
            API = "https://www.googleapis.com/books/v1/volumes?fields=items(selfLink,volumeInfo(title,subtitle,authors,imageLinks))&q={}&maxResults=40&printType=books".format(nameBook)
            r = requests.get(url=API, headers=headers)
            if r.status_code == 200:
                data = json.loads(r.content)
                n = 0
                break
     
    return window_searchInput, data, n, headers
    
# window_searchInput, data, n, headers = searchInput()