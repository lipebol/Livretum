import PySimpleGUI as sg
import os
from cryptography.fernet import Fernet
from files_app.conn_MongoDB import inputConnMongoDB


def inputPath():

    sg.theme('DarkGrey11')

    logo = sg.Image(filename='files_app/images/Livretum.png')
    question_path = sg.Text("Onde estão as credenciais do MongoDB?", font='Courier 14')
    version = sg.Text("v 0.2", font='Courier 8')

    layout_inputPath = [
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

    window_inputPath = sg.Window(
        "Livretum",
        icon='files_app/images/icon_Livretum.png',
        layout=layout_inputPath,
        size=(500, 410),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c'
    )

    path = None
    conn_type = None

    while True:
        event, values = window_inputPath.read()
        if event == sg.WIN_CLOSED:
            return path, conn_type
            break
        if event == "OK":
            if values["pathAuthMongoDB"] == "":
                window_inputPath.Hide()
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
                window_inputPath.Hide()
                return path, conn_type
                break


def noFile():
    sg.theme('DarkGrey11')

    messagenoFile = sg.Text(
        "[!] Arquivo com credenciais não encontrado.\n        Informe o arquivo novamente."
    , font='Courier 14')
   
    layout_noFile = [
        [sg.Text('')],
        [sg.Column([[messagenoFile]])],
    ]

    window_noFile = sg.Window(
        "?!",
        icon='files_app/images/icon_Livretum.png',
        layout = layout_noFile,
        size=(600, 100),
        resizable = True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c',
    )

    while True:
        event, values = window_noFile.read()
        if event == sg.WIN_CLOSED:
            break


def encryptPath(directory, path, conn_type):
    with open(f"{directory}/.ps.key", "rb") as ps:
        key = ps.read()
    fernet = Fernet(key)
    path = path.encode()
    encrypted = fernet.encrypt(path)
    with open(f"{directory}/.path", "wb") as encrypt_file:
        encrypt_file.write(encrypted)
    with open(f"{directory}/.type", "w") as type_file:
        type_file.write(conn_type)


def verifyAuth(directory, user_bookcase):
    try:
        with open(f"{directory}/.ps.key", "rb") as ps:
            key = ps.read()
        with open(f"{directory}/.path", "rb") as encrypt_file:
            encrypted = encrypt_file.read()
        fernet = Fernet(key)
        auth_path = fernet.decrypt(encrypted).decode()
        auth = open(auth_path).read().strip().split("=")
    except FileNotFoundError:
        os.remove(f"{directory}/.path")
        os.remove(f"{directory}/.type")
        user = None
        pwd = None
        return user, pwd
    else:
        user = auth[0]
        pwd = auth[1]
        return user, pwd

def inputUser():

    sg.theme('DarkGrey11')

    logo = sg.Image(filename='files_app/images/Livretum.png')
    question_user_bookcase = sg.Text("Quem é o dono da estante?", font='Courier 14')
    user_bookcase = sg.InputText('', key="user_bookcase", size=(26), font='Courier 14')
    version = sg.Text("v 0.2", font='Courier 8')

    layout_inputUser = [ 
        [sg.Text('')],
        [sg.Column([[logo]])],
        [sg.Text('')],
        [sg.Column([[question_user_bookcase]])],
        [sg.Column([[user_bookcase]])],
        [sg.Text('')],
        [sg.Button("Enviar", font='Courier 12')],
        [sg.Text('')],
        [sg.Column([[version]])]
    ]
    
    window_inputUser = sg.Window(
        "Livretum",
        icon='files_app/images/icon_Livretum.png',
        layout=layout_inputUser,
        size=(500, 360),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9,
        element_justification='c'
    )

    while True:
        event, values = window_inputUser.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Enviar":
            if values["user_bookcase"] != "":
                directory = os.path.expanduser('~/.docs_Livretum/')
                files = os.listdir(directory)
                window_inputUser.Hide()
                if ".path" not in files:
                    path, conn_type = inputPath()
                    if path == None or conn_type == None:
                        break
                    else:
                        encryptPath(directory, path, conn_type)
                user_bookcase = values["user_bookcase"]
                user, pwd = verifyAuth(directory, user_bookcase)
                if user == None or pwd == None:
                    noFile()
                    window_inputUser.UnHide()
                else:
                    inputConnMongoDB(directory, user_bookcase, user, pwd)
                    window_inputUser.UnHide()



# def myBookcase():

#     sg.theme('DarkGrey11')
    
#     dataFrame = pd.read_sql_query("""
#     SELECT c.Nome, e.Tipo, e.Modalidade, e.Valor
#     FROM Clientes AS c, Forma_Pagamento AS d, Planos AS e
#     WHERE c.Id_Forma_Pagamento = d.Id AND c.Id_Planos = e.Id
#     """, conn)
#     headings = list(dataFrame.columns)
#     values = dataFrame.values.tolist()

#     layout_dataFrameCustomers = [
#         [sg.Text('')],
#         [sg.Table(values = values, headings = headings, auto_size_columns=True)],
#         [sg.Text('')],
#         [sg.Text("v 0.1", font='Courier 8')]
#     ]

#     window_dataFrameCustomers = sg.Window("chEx", icon='files_app/images/chEx-icon.png', 
#     layout = layout_dataFrameCustomers, size=(400, 240), resizable=True, element_justification='c', 
#     finalize=True)

#     while True:
#         event, values = window_dataFrameCustomers.read()
#         if event == sg.WIN_CLOSED:
#             break