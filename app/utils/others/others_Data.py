import PySimpleGUI as sg
from utils.window.location import location
from utils.notifications.no_Data import noData

def othersData():

    sg.theme('DarkGrey11')

    x = 600
    y = 440

    size_x, size_y = location(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    question_collection = sg.Text("Coleção:", font='Courier 14')
    collection_input = sg.InputText('', key="collection", size=(30), font='Courier 14')
    question_status = sg.Text("Adquirido?", font='Courier 14')

    layout_othersData = [
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Column([[question_collection]])],
        [sg.Column([[collection_input]])],
        [sg.Text('')],
        [sg.Column([[question_status]])],
        [sg.Checkbox("Sim", key='yes', font='Courier 14'),
        sg.Checkbox("Não", key='no', font='Courier 14')],
        [sg.Text('')],
        [sg.Button("Enviar", font='Courier 12')],
        [sg.Text('')],
    ]

    window_othersData = sg.Window(
        "Livretum",
        icon='app/src/images/icon_Livretum.png',
        layout = layout_othersData,
        size=(x, y),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(size_x, size_y)
    )

    while True:
        event, values = window_othersData.read()
        if event == sg.WIN_CLOSED:
            return "Exit", "Exit"
            break
        if values["collection"] == "" or values["yes"] == False and values["no"] == False:
            window_othersData.Hide()
            noData()
            othersData()
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
