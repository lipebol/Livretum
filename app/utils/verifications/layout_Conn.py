import PySimpleGUI as sg


def layout_Conn(
    directory, MongoDB_logo, user, len_pwd, addr, database, testMongoDB, version
):
    conn_type = open(f"{directory}/.type_mongodb").read().strip()
    if conn_type == "Local":
        layout_connMongoDB = [
            [sg.Text('')],
            [sg.Column([[MongoDB_logo]], justification='center')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text(f"Usuário: {user}", font='Courier 14')],
            [sg.Text('')],
            [sg.Text(f"Senha: {len_pwd}", font='Courier 14')],
            [sg.Text('')],
            [sg.Text(f"Host: @{addr}:27017", font='Courier 14')],
            [sg.Text('')],
            [sg.Text(f"Database: {database}", font='Courier 14')],
            [sg.Text('')],
            [sg.Column([[testMongoDB]], justification='center')],
            [sg.Text('')],
            [sg.Column([[version]], justification="center")]
        ]
    if conn_type == "Atlas":
        layout_connMongoDB = [
            [sg.Text('')],
            [sg.Column([[MongoDB_logo]], justification='center')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text(f"Usuário: {user}", font='Courier 14')],
            [sg.Text('')],
            [sg.Text(f"Senha: {len_pwd}", font='Courier 14')],
            [sg.Text('')],
            [sg.Text(f"Cluster: @{addr}", font='Courier 14')],
            [sg.Text('')],
            [sg.Text(f"Database: {database}", font='Courier 14')],
            [sg.Text('')],
            [sg.Column([[testMongoDB]], justification='center')],
            [sg.Text('')],
            [sg.Column([[version]], justification="center")]
        ]

    return conn_type, layout_connMongoDB