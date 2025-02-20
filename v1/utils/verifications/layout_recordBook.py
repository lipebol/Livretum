import PySimpleGUI as sg
import textwrap
from utils.verifications.extract_Two import extractTwo

def layoutrecordBook(url_book, collection, acquired):

    logo = sg.Image(filename='app/src/images/Livretum.png')
    confirm_data_book = sg.Text("Dados do Livro", font='Courier')
    if type(url_book) != dict:
        item = extractTwo(url_book, acquired)
    else:
        item = url_book
        wrapperI = textwrap.TextWrapper(width=45)
        wrapperII = textwrap.TextWrapper(width=35)
        item["título"] = wrapperI.fill(text=item["título"])
        item["autor(es)"] = wrapperII.fill(text=item["autor(es)"])

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
        [sg.Text(f'Loja: {item["loja"]}', font='Courier')],
        [sg.Text(f'Avaliação: {item["avaliação"]}', font='Courier')],
        [sg.Text(f'Preço: {item["preço"]}', font='Courier')],
        [sg.Text(f'Adquirido?: {item["Adquirido?"]}', font='Courier')],
        [sg.Text('')],
        [sg.Button("Cadastrar", font='Courier')],
        [sg.Text('')]
    ]

    return layout_recordBook