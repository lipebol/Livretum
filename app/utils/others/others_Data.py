import PySimpleGUI as sg
from utils.notifications.no_Data import noData
from utils.window.icon import icon
from utils.window.screen import screen


def othersData():

    sg.theme('DarkGrey11')

    x, y = 0.43923865300146414, 0.5729166666666666
    size_x, size_y, loc_x, loc_y = screen(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    question_collection = sg.Text("Coleção:", font='Courier')
    collection_input = sg.InputText('', key="collection", size=(30), font='Courier', focus=True)
    question_status = sg.Text("Adquirido?", font='Courier')
    system_icon = icon()

    layout_othersData = [
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Column([[question_collection]])],
        [sg.Column([[collection_input]])],
        [sg.Text('')],
        [sg.Column([[question_status]])],
        [sg.Checkbox("Sim", key='yes', font='Courier'),
        sg.Checkbox("Não", key='no', font='Courier')],
        [sg.Text('')],
        [sg.Button("Enviar", font='Courier')],
        [sg.Text('')],
    ]

    window_othersData = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_othersData,
        size=(size_x, size_y),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(loc_x, loc_y)
    )

    while True:
        event, values = window_othersData.read()
        if event == sg.WIN_CLOSED:
            return "Exit", "Exit"
            break
        if values["collection"] == "" or values["yes"] == False and values["no"] == False:
            window_othersData.Hide()
            noData()
            return "Repeat", "Repeat"
            break
        else:
            if event == "Enviar":
                window_othersData.Hide()
                collection = values["collection"]
                yes = values["yes"]
                no = values["no"]
                if yes == True:
                    status = "Sim"
                    return collection, status
                    break
                if no == True:
                    status = "Não"
                    return collection, status
                    break
