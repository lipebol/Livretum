import PySimpleGUI as sg


def inputAuth():

    sg.theme('DarkGrey11')

    logo = sg.Image(filename='src/images/Livretum.png')
    question_path = sg.Text("Onde estão as credenciais do MongoDB?", font='Courier 14')
    version = sg.Text("v 0.2", font='Courier 8')

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
        icon='src/images/icon_Livretum.png',
        layout=layout_pathAuth,
        size=(500, 410),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c'
    )

    path = None
    conn_type = None

    while True:
        event, values = window_pathAuth.read()
        if event == sg.WIN_CLOSED:
            return path, conn_type
            break
        if event == "OK":
            path_Auth = values["pathAuthMongoDB"]
            if path_Auth == "":
                window_pathAuth.Hide()
                return path, conn_type
                break
            else:
                path = values["pathAuthMongoDB"]
                type_local = values["type_local"]
                type_atlas = values["type_atlas"]
                if type_local == True:
                    conn_type = "Local"
                if type_atlas == True:
                    conn_type = "Atlas"
                window_pathAuth.Hide()
                return path, conn_type
                break