import PySimpleGUI as sg
from utils.verifications.extract_Two import extractTwo

def layoutrecordBook(URL_book, collection, status):

    logo = sg.Image(filename='app/src/images/Livretum.png')
    confirm_data_book = sg.Text("Dados do Livro", font='Courier')
    item = extractTwo(URL_book, status)

    layout_recordBook = [
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Column([[confirm_data_book]])],
        [sg.Text(f'{item["título"]}', font='Courier')],
        [sg.Text(f'Autor(es): {item["autor(es)"]}', font='Courier')],
        [sg.Text(f'Editora: {item["editora"]}', font='Courier')],
        [sg.Text(f'Publicação: {item["data_da_publicação"]}', font='Courier')],
        [sg.Text(f'ISBN-10: {item["isbn_10"]}', font='Courier')],
        [sg.Text(f'ISBN-13: {item["isbn_13"]}', font='Courier')],
        [sg.Text(f'Páginas: {item["páginas"]}', font='Courier')],
        [sg.Text(f'Coleção: {collection}', font='Courier')],
        [sg.Text(f'Adquirido?: {item["Adquirido?"]}', font='Courier')],
        [sg.Text(f'Avaliação: {item["avaliação"]}', font='Courier')],
        [sg.Text(f'Preço: {item["preço"]}', font='Courier')],
        [sg.Text('')],
        [sg.Button("Cadastrar", font='Courier')],
        [sg.Text('')]
    ]

    return layout_recordBook