import PySimpleGUI as sg
from utils.verifications.ack_Id import ackId
from utils.window.icon import icon
from utils.window.screen import screen


def changedStatus(user_bookcase, itens):

    sg.theme('DarkGrey11')

    x, y = 0.24890190336749635, 0.2734375
    size_x, size_y, loc_x, loc_y = screen(x, y)


    id_changed = sg.Text("Qual o 'id' do livro?", font='Courier')
    id = sg.InputText('', key="id", size=(15), font='Courier', focus=True)
    system_icon = icon()

    layout_changedStatus = [
        [sg.Text('')],
        [sg.Column([[id_changed]])],
        [sg.Text('')],
        [sg.Column([[id]])],
        [sg.Text('')],
        [sg.Button("Enviar", font='Courier', bind_return_key=True)],
    ]
    
    window_changedStatus = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_changedStatus,
        size=(size_x, size_y),
        resizable=True,
        grab_anywhere=True,
        element_justification='c',
        location=(loc_x, loc_y)
    )

    while True:
        event, values = window_changedStatus.read()
        if event == sg.WIN_CLOSED:
            return "Exit"
            break
        if event == "Enviar":
            id = values["id"]
            if id != "":
                if id.isdigit() == True:
                    if int(id) <= len(itens):
                        window_changedStatus.Hide()
                        ack = ackId(user_bookcase, itens[int(id)-1])
                        if ack != "Exit":
                            return "Reload"
                            break
                        else:
                            return "Exit"
                            break