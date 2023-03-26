import PySimpleGUI as sg
from utils.verifications.extract_Two import extractTwo

def layoutrecordBook(URL_book, collection, status):

    logo = sg.Image(filename='app/src/images/Livretum.png')
    confirm_data_book = sg.Text("Dados do Livro", font='Courier 14')
    title, authors, pub_company, pub_date, isbn_10, isbn_13, pages, categories, rating, price = extractTwo(URL_book)

    layout_recordBook = [
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Column([[confirm_data_book]])],
        [sg.Text(f"{title}", font='Courier 12')],
        [sg.Text(f"Autor(es): {authors}", font='Courier 12')],
        [sg.Text(f"Editora: {pub_company}", font='Courier 12')],
        [sg.Text(f"Publicação: {pub_date}", font='Courier 12')],
        [sg.Text(f"ISBN-10: {isbn_10}", font='Courier 12')],
        [sg.Text(f"ISBN-13: {isbn_13}", font='Courier 12')],
        [sg.Text(f"Páginas: {pages}", font='Courier 12')],
        [sg.Text(f"Coleção: {collection}", font='Courier 12')],
        [sg.Text(f"Adquirido?: {status}", font='Courier 12')],
        [sg.Text(f"Avaliação: {rating}", font='Courier 12')],
        [sg.Text(f"Preço: {price}", font='Courier 12')],
        [sg.Text('')],
        [sg.Button("Cadastrar", font='Courier 12')],
        [sg.Text('')]
    ]

    return layout_recordBook