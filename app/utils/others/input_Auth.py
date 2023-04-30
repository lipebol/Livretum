import PySimpleGUI as sg
from utils.notifications.file_Format import fileFormat
from utils.notifications.no_Data import noData
from utils.window.icon import icon
from utils.window.screen import screen


def inputAuth():

    sg.theme('DarkGrey11')

    x, y = 0.36603221083455345, 0.5338541666666666
    size_x, size_y, loc_x, loc_y = screen(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    question_path = sg.Text("Onde está o 'arquivo.txt'?", font='Courier')
    system_icon = icon()
    fileFormat()

    layout_pathAuth = [
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Column([[question_path]])],
        [sg.InputText("", key="pathAuthMongoDB", size=(26), font='Courier'),
        sg.FileBrowse("Procurar", font='Courier')],
        [sg.Text('')],
        [sg.Checkbox("Local", key='type_local', font='Courier'), 
        sg.Checkbox("Atlas", key='type_atlas', font='Courier')],
        [sg.Text('')],
        [sg.Button("OK", font='Courier')]
    ]

    window_pathAuth = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_pathAuth,
        size=(size_x, size_y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(loc_x, loc_y)
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