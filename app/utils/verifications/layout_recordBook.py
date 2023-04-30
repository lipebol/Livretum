import PySimpleGUI as sg
from utils.verifications.extract_Two import extractTwo

def layoutrecordBook(URL_book, collection, status):

    logo = sg.Image(filename='app/src/images/Livretum.png')
    confirm_data_book = sg.Text("Dados do Livro", font='Courier')
    title, authors, pub_company, pub_date, isbn_10, isbn_13, pages, categories, rating, price = extractTwo(URL_book)

    layout_recordBook = [
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Column([[confirm_data_book]])],
        [sg.Text(f"{title}", font='Courier')],
        [sg.Text(f"Autor(es): {authors}", font='Courier')],
        [sg.Text(f"Editora: {pub_company}", font='Courier')],
        [sg.Text(f"Publicação: {pub_date}", font='Courier')],
        [sg.Text(f"ISBN-10: {isbn_10}", font='Courier')],
        [sg.Text(f"ISBN-13: {isbn_13}", font='Courier')],
        [sg.Text(f"Páginas: {pages}", font='Courier')],
        [sg.Text(f"Coleção: {collection}", font='Courier')],
        [sg.Text(f"Adquirido?: {status}", font='Courier')],
        [sg.Text(f"Avaliação: {rating}", font='Courier')],
        [sg.Text(f"Preço: {price}", font='Courier')],
        [sg.Text('')],
        [sg.Button("Cadastrar", font='Courier')],
        [sg.Text('')]
    ]

    return layout_recordBook