from dotenv import load_dotenv
from os import getenv
import PySimpleGUI as sg
from utils.check import Check
from utils.notify import Notify
from utils.set import Set


class App:

    load_dotenv()
    sg.theme(getenv('THEME'))
    def __init__(self):
        self.logo, self.icon = Set().logo(), Set().icon()
        self.size_x, self.loc_x, self.size_y, self.loc_y = tuple(
            Set().screen((0.36603221083455345, 0.46875))
        )


    def user(self):
        try:
            self.userWindow = sg.Window(
                getenv('NAME'), icon=self.icon, layout=[ 
                    [sg.Text('')],
                    [sg.Column([[sg.Image(filename=self.logo)]])],
                    [sg.Text('')],
                    [
                        sg.Column([[sg.Text('Quem é o dono da estante?', font=getenv('DEFAULT_FONT'))]])
                    ],
                    [
                        sg.Column(
                            [[
                                sg.InputText(
                                    '', key='user', size=(20), font=getenv('DEFAULT_FONT'), focus=True
                                )
                            ]]
                        )
                    ],
                    [sg.Text('')],
                    [sg.Button('Enviar', font=getenv('DEFAULT_FONT'), bind_return_key=True)]
                ],
                size=(self.size_x, self.size_y), resizable=True, grab_anywhere=True, 
                alpha_channel=.9, element_justification='c', location=(self.loc_x, self.loc_y)
            )

            while True:
                event, values = self.userWindow.read()
                if event == sg.WIN_CLOSED:
                    return 'Exit'
                    break
                if event == 'Enviar':
                    if values['user']:
                        self.userWindow.Hide()
                        if not Check().db():
                            if Notify().hasWebhook():
                                return 'Exit'
                            return Set().db(values['user'])
                        return Check().username(values['user'])
        except Exception as error:
            print(error)
            return 'Error'


    def bookcase(self, user: tuple):
        try:
            self.this_size_x, self.this_loc_x, self.this_size_y, self.this_loc_y = tuple(
                Set().screen((0.541727672035139, 0.5989583333333334))
            )
            self.bookcaseWindow = sg.Window(
                getenv('NAME'), icon=self.icon, layout=Set().bookcase(user), 
                size=(self.this_size_x, self.this_size_y), resizable=True, 
                grab_anywhere=True, alpha_channel=.9, element_justification='c', 
                location=(self.this_loc_x, self.this_loc_y)
            )

            while True:
                event, values = self.bookcaseWindow.read()
                if event == sg.WIN_CLOSED:
                    return 'Exit'
                    break
                if event == 'Novo Livro':
                    return 'Reload'
        except Exception as error:
            print(error)
            return 'Error'


    def start(self):
        if not Check().connection():
            Notify().noNet()
        else:
            if Set().dir():
                self.mainWindow = sg.Window(
                    getenv('NAME'), icon=self.icon, layout=[
                        [sg.Text('')],
                        [
                            sg.Column(
                                [[sg.Image(filename=self.logo)]], 
                                justification=getenv('DEFAULT_JUSTIFICATION')
                            )
                        ],
                        [sg.Text('')],
                        [sg.Text('')],
                        [
                            sg.Column(
                                [[sg.Button('Minha Estante', font=getenv('DEFAULT_FONT'))]], 
                                justification=getenv('DEFAULT_JUSTIFICATION')
                            )
                        ],
                        [
                            sg.Column(
                                [[
                                    sg.Button(
                                        'Recomendações', font=getenv('DEFAULT_FONT'), disabled=True
                                    )
                                ]], 
                                justification=getenv('DEFAULT_JUSTIFICATION')
                            )
                        ],
                        [sg.Text('')]
                    ], 
                    size=(self.size_x, self.size_y), resizable=True, grab_anywhere=True, 
                    alpha_channel=.9, location=(self.loc_x, self.loc_y)
                )

                while True:
                    event, values = self.mainWindow.read()
                    if event == sg.WIN_CLOSED:
                        break
                    if event == 'Minha Estante':
                        self.mainWindow.Hide()
                        self.__user = self.user()
                        if self.__user not in ('Error', 'Exit'):
                            while self.bookcase(self.__user) == 'Reload':
                                continue
                    self.mainWindow.UnHide()

if __name__ == '__main__':
    App().start()
        