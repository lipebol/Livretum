import PySimpleGUI as sg
import json
from utils.notifications.no_Data import noData
from utils.verifications.scrape import Scrape
from utils.window.icon import icon
from utils.window.screen import screen


def inputManually():

    sg.theme('DarkGrey11')

    x, y = 0.35871156661786235, 0.6510416666666666
    size_x, size_y, loc_x, loc_y = screen(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    title = sg.Text("Título:", font='Courier')
    input_title = sg.InputText('', key="title", size=(35), font='Courier')
    authors = sg.Text("Autor(es):", font='Courier')
    input_authors = sg.InputText('', key="authors", size=(32), font='Courier')
    pub_company = sg.Text("Editora:", font='Courier')
    input_pub_company = sg.InputText('', key="pub_company", size=(34), font='Courier')
    pub_date = sg.Text("Dt.Publicação:", font='Courier')
    isbn10 = sg.Text("ISBN-10:", font='Courier')
    input_isbn10 = sg.InputText('', key="isbn10", size=(10), font='Courier')
    isbn13 = sg.Text("ISBN-13:", font='Courier')
    input_isbn13 = sg.InputText('', key="isbn13", size=(13), font='Courier')
    pages = sg.Text("Qt.Páginas:", font='Courier')
    input_pages = sg.InputText('', key="pages", size=(4), font='Courier')
    system_icon = icon()

    layout_inputManually = [ 
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Column([[title]], justification='l'), sg.Column([[input_title]])],
        [sg.Column([[authors]], justification='l'), sg.Column([[input_authors]])],
        [sg.Column([[pub_company]], justification='l'), sg.Column([[input_pub_company]])],
        [sg.Column([[pub_date]], justification='l'), 
        sg.Input(key="pub_date", size=(8), font='Courier'), 
        sg.CalendarButton(
            '...', title='Calendário', format='%d/%m/%y', no_titlebar=False, font='Courier 8',
        month_names=(
            'Janeiro', 'Fevereiro', 'Março', 
            'Abril', 'Maio', 'Junho', 
            'Julho', 'Agosto', 'Setembro', 
            'Outubro', 'Novembro', 'Dezembro'
        ), 
        day_abbreviations=('dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sáb'))],
        [sg.Column([[isbn10]], justification='l'), sg.Column([[input_isbn10]])],
        [sg.Column([[isbn13]], justification='l'), sg.Column([[input_isbn13]])],
        [sg.Column([[pages]], justification='l'), sg.Column([[input_pages]])],
        [sg.Text('')],
        [sg.Button("Enviar", font='Courier', bind_return_key=True)]
    ]
    
    window_inputManually = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_inputManually,
        size=(size_x, size_y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(loc_x, loc_y)
    )

    while True:
        event, values = window_inputManually.read()
        if event == sg.WIN_CLOSED:
            return "Exit"
            break
        if event == "Enviar":
            title = values["title"]
            authors = values["authors"]
            pub_company = values["pub_company"]
            pub_date = values["pub_date"]
            isbn10 = values["isbn10"]
            isbn13 = values["isbn13"]
            pages = values["pages"]
            testOne = title == "" or authors == "" or pub_company == ""
            testTwo = pub_date == "" or isbn10 == "" or isbn13 == ""
            if testOne == True or testTwo == True or pages == "":
                noData()
            else:
                window_inputManually.Hide()
                rating, price = Scrape(title)
                item = {
                    "categoria(s)": "manually",
                    "título": title,
                    "autor(es)": authors,
                    "editora": pub_company,
                    "data_da_publicação": pub_date,
                    "isbn_10": isbn10,
                    "isbn_13": isbn13,
                    "páginas": pages,
                    "avaliação": rating,
                    "preço": price,
                }

                return item
                break

                