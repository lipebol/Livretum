import PySimpleGUI as sg
from utils.notifications.no_Data import noData
from utils.verifications.separator_Auth import separatorAuth
from utils.window.icon import icon
from utils.window.screen import screen


def inputAuth():

    sg.theme('DarkGrey11')

    x, y = 0.36603221083455345, 0.5338541666666666
    size_x, size_y, loc_x, loc_y = screen(x, y)

    logo = sg.Image(filename='app/src/images/Livretum.png')
    question_path = sg.Text("Onde está o 'arquivo.txt'?", font='Courier')
    system_icon = icon()

    layout_inputAuth = [
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Column([[question_path]])],
        [sg.InputText("", key="inputAuth", size=(20), font='Courier'),
        sg.FileBrowse("Procurar", font='Courier', file_types=(("", "*.txt"),))],
        [sg.Text('')],
        [sg.Checkbox("Local", key='type_local', font='Courier'), 
        sg.Checkbox("Atlas", key='type_atlas', font='Courier')],
        [sg.Text('')],
        [sg.Button("OK", font='Courier')]
    ]

    window_inputAuth = sg.Window(
        "Livretum",
        icon=system_icon,
        layout=layout_inputAuth,
        size=(size_x, size_y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
        location=(loc_x, loc_y)
    )

    while True:
        event, values = window_inputAuth.read()
        if event == sg.WIN_CLOSED:
            return "Exit", "Exit"
            break
        if event == "OK":
            path = values["inputAuth"]
            type =  values["type_local"] == False and values["type_atlas"] == False
            if path == "" or type == True:
                noData()
            else:
                window_inputAuth.Hide()
                try:
                    auth = open(path).read().strip()
                except (UnicodeDecodeError):
                    return "Exit", "Exit"
                separator = separatorAuth(auth)
                if separator == True:
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
                else:
                    return "Exit", "Exit"
                    break
                    