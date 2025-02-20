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
            [sg.Text("[❗] Nenhum livro cadastrado.", font='Courier')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Button("Novo Livro", font='Courier')]
        ]
    else:
        button_new = sg.Button("Novo Livro", font='Courier')
        button_status = sg.Button("Adquirido?", font='Courier')
        layout_myBookcase = [
            [sg.Text('')],
            [sg.Column([[logo]])],
            [sg.Table(
                values=values, 
                headings=cols, 
                auto_size_columns=True, 
                font='Courier', 
                justification='center'
                )
            ],
            [sg.Text('')],
            [sg.Column([[button_new]]), sg.Column([[button_status]])]
        ]

    return layout_myBookcase