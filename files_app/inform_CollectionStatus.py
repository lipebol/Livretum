import PySimpleGUI as sg

def collectionStatus():

    sg.theme('DarkGrey11')

    logo = sg.Image(filename='files_app/images/Livretum.png')
    questionCollection = sg.Text("Coleção:", font='Courier 14')
    collectionInput = sg.InputText('', key="collection", size=(30), font='Courier 14')
    questionStatus = sg.Text("Adquirido?", font='Courier 14')
#    statusInput = sg.InputText('', key="status", size=(30), font='Courier 14')

    layout_collectionStatus = [
        [sg.Text("")],
        [sg.Column([[logo]])],
        [sg.Text("")],
        [sg.Text("")],
        [sg.Column([[questionCollection]])],
        [sg.Column([[collectionInput]])],
        [sg.Text("")],
        [sg.Column([[questionStatus]])],
        [sg.Checkbox("Sim", key='status', font='Courier 14'), 
        sg.Checkbox("Não", key='status', font='Courier 14')],
    #    [sg.Column([[statusInput]])],
        [sg.Text("")],
        [sg.Button("Enviar", font='Courier 12')],
        [sg.Text("")],
    ]

    window_collectionStatus = sg.Window(
        "Livretum",
        icon='files_app/images/icon_Livretum.png',
        layout = layout_collectionStatus,
        size=(600, 440),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c'
    )

    while True:
        event, values = window_collectionStatus.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Enviar":
            collection = values["collection"]
            status = values["status"]
            if status == True:
                status = "Sim"
            if status == False:
                status = "Não"
            break

    return window_collectionStatus, collection, status

window_collectionStatus, collection, status = collectionStatus()