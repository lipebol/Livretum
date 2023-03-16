import PySimpleGUI as sg
from files_app.search_API import data, n, headers
from files_app.search_API import window_searchInput
import textwrap
import requests
from PIL import Image


def confirmSearch():
    global n, URL_book
     #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}

    sg.theme('DarkGrey11')
    window_searchInput.hide()
    wrapperI = textwrap.TextWrapper(width=42)
    wrapperII = textwrap.TextWrapper(width=35)

    selector = data['items'][n]['volumeInfo']
    if 'subtitle' not in selector:
        title = "".join(data['items'][n]['volumeInfo']['title'])
    else:
        title = data['items'][n]['volumeInfo']['title'],"-", data['items'][n]['volumeInfo']['subtitle']
        title = " ".join(title)
        title = wrapperI.fill(text=title)
        title = "".join(title)
    if 'authors' not in selector:
        authors = None
    else:
        authors = ", ".join(data['items'][n]['volumeInfo']['authors'])
        authors = wrapperII.fill(text=authors)
        authors = "".join(authors)
    if 'imageLinks' not in selector:
        pass
    else:
        URL_image = data['items'][n]['volumeInfo']['imageLinks']['smallThumbnail']
        r = requests.get(url=URL_image, headers=headers, stream=True)
        if r.status_code == 200:
            with open('files_app/images/book.jpeg', 'wb') as image:
                image.write(r.content)
            image = Image.open('files_app/images/book.jpeg')
            image.save('files_app/images/book.png')
            
    logo = sg.Image(filename='files_app/images/Livretum.png')
    confirm_Book = sg.Text("É esse o livro?", font='Courier 14')
    bookImage = sg.Image(filename='files_app/images/book.png')
    textTitle = sg.Text("Nome: {} ".format(title), font='Courier 14')
    textAuthors = sg.Text("Autor(es): {} ".format(authors), font='Courier 14')
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
        icon='files_app/images/icon_Livretum.png',
        layout = layout_confirmSearch, 
        size=(600, 620),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
    )

    while True:
        event, values = window_confirmSearch.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Não":
            n += 1
            window_confirmSearch.hide()
            confirmSearch()
            break
        if event == "Sim":
            URL_book = data['items'][n]['selfLink'] + "?fields=volumeInfo"
            window_confirmSearch.hide()
            break

    return window_confirmSearch

confirmSearch()