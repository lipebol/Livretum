import PySimpleGUI as sg
import os
from cryptography.fernet import Fernet
from src.conn_MongoDB import ConnMongoDB
from files_app.utils import noFile, encryptPath, verifyAuth







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