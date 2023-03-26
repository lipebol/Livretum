import PySimpleGUI as sg


def layoutmyBookcase(logo, cols, values):
    if cols == "No Records" or values == "No Records":
        layout_myBookcase = [
            [sg.Text('')],
            [sg.Column([[logo]])],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text("[❗] Nenhum livro cadastrado.", font='Courier 14')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Button("Novo Livro", font='Courier 12'), 
            sg.Button("🔄", font='Courier 12')],
            [sg.Text('')],
            [sg.Text("v 0.2", font='Courier 8')]
        ]
    else:
        layout_myBookcase = [
            [sg.Text('')],
            [sg.Column([[logo]])],
            [sg.Table(values=values, headings=cols, auto_size_columns=True, font='Courier 12')],
            [sg.Text('')],
            [sg.Button("Novo Livro", font='Courier 12'),
            sg.Button("🔄", font='Courier 12')],
            [sg.Text('')],
            [sg.Text("v 0.2", font='Courier 8')]
        ]

    return layout_myBookcase