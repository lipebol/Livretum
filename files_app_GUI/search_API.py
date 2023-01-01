# apt install python3-tk

import PySimpleGUI as sg
import requests
import json


def searchInput():
#    global n, data
     #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
    
    sg.theme('DarkGrey11')

    jBook = sg.Image(filename='archives_app_GUI/images/jBook.png')
    search = sg.Text("Autor ou Assunto: ", font='Courier 14')
    searchInput = sg.InputText('', key="nameBook", size=(26), font='Courier 14')

    layout_searchInput = [
        [sg.Text('')],
        [sg.Column([[jBook]])],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Column([[search]])],
        [sg.Column([[searchInput]])],
        [sg.Text('')],
        [sg.Button("Pesquisar", font='Courier 12')],
        [sg.Text('')],
    ]

    window_searchInput = sg.Window("jBook", icon='archives_app_GUI/images/j.png',
    layout = layout_searchInput, size=(400,360),resizable = True, element_justification='c', 
    finalize=True)

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
    
window_searchInput, data, n, headers = searchInput()