import PySimpleGUI as sg
from utils.window.location import location
from utils.notifications.file_Format import fileFormat
from utils.notifications.no_Data import noData


def inputAuth():

    sg.theme('DarkGrey11')

    x = 500
    y = 410

    size_x, size_y = location(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    question_path = sg.Text("Onde está o 'arquivo.txt'?", font='Courier 14')
    version = sg.Text("v 0.2", font='Courier 8')
    fileFormat()

    layout_pathAuth = [
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Column([[question_path]])],
        [sg.InputText("", key="pathAuthMongoDB", size=(26), font='Courier 12'),
        sg.FileBrowse("Procurar", font='Courier 10')],
        [sg.Text('')],
        [sg.Checkbox("Local", key='type_local', font='Courier 14'), 
        sg.Checkbox("Atlas", key='type_atlas', font='Courier 14')],
        [sg.Text('')],
        [sg.Button("OK", font='Courier 12')],
        [sg.Text('')],
        [sg.Column([[version]])]
    ]

    window_pathAuth = sg.Window(
        "Livretum",
        icon='app/src/images/icon_Livretum.png',
        layout=layout_pathAuth,
        size=(x, y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(size_x, size_y)
    )

    while True:
        event, values = window_pathAuth.read()
        if event == sg.WIN_CLOSED:
            return "Exit", "Exit"
            break
        if values["pathAuthMongoDB"] == "" or values["type_local"] == False and values["type_atlas"] == False:
            window_pathAuth.Hide()
            noData()
            return "Repeat", "Repeat"
            break
        else:
            if event == "OK":
                window_pathAuth.Hide()
                path = values["pathAuthMongoDB"]
                type_local = values["type_local"]
                type_atlas = values["type_atlas"]
                if type_local == True:
                    conn_type = "Local"
                    return path, conn_type
                    break
                if type_atlas == True:
                    conn_type = "Atlas"
                    return path, conn_type
                    break