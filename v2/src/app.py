from dotenv import load_dotenv
from os import getenv
import PySimpleGUI as sg
from utils.check import Check
from utils.set import Set


class App:

    load_dotenv()
    sg.theme(getenv('THEME'))
    def __init__(self):
        self.logo, self.icon = Set().logo(), Set().icon()
        (self.size_x, self.loc_x, self.size_y, self.loc_y) = tuple(
            Set().screen((0.36603221083455345, 0.390625))
        )

    def user(self):
        self.userWindow = sg.Window(
            getenv('NAME'), icon=self.icon, layout=[ 
                [sg.Text('')],
                [sg.Column([[self.logo]])],
                [sg.Text('')],
                [sg.Column([[sg.Text('Quem é o dono da estante?', font=getenv('DEFAULT_FONT'))]])],
                [sg.Column([[sg.InputText('', key='user', size=(20), font=getenv('DEFAULT_FONT'), focus=True)]])],
                [sg.Text('')],
                [sg.Button('Enviar', font=getenv('DEFAULT_FONT'), bind_return_key=True)]
            ],
            size=(self.size_x, self.size_y), resizable=True, grab_anywhere=True, 
            alpha_channel=.9, element_justification='c', location=(self.loc_x, self.loc_y)
        )

        while True:
            event, values = self.userWindow.read()
            if event == sg.WIN_CLOSED:
                return "Exit"
                break
            if event == "Enviar":
                if values['user']:
                    print(values['user'])

    def run(self):
        if Check().connection() and Set().dir():
            self.mainWindow = sg.Window(
                getenv('NAME'), icon=self.icon, layout=[
                    [sg.Text('')],
                    [
                        sg.Column(
                            [[sg.Image(filename=self.logo)]], justification=getenv('DEFAULT_JUSTIFICATION')
                        )
                    ],
                    [sg.Text('')],
                    [
                        sg.Column(
                            [[sg.Button('Minha Estante', font=getenv('DEFAULT_FONT'))]], 
                            justification=getenv('DEFAULT_JUSTIFICATION')
                        )
                    ],
                    [
                        sg.Column(
                            [[sg.Button('Recomendações', font=getenv('DEFAULT_FONT'), disabled=True)]], 
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
                #user_bookcase = userBookcase()
                #if user_bookcase != "Exit":
                #    if user_bookcase != "Error":
                #        status = "Reload"
                #        while status == "Reload":
                #            status = myBookcase(user_bookcase)
            self.mainWindow.UnHide()

if __name__ == '__main__':
    App().run()
        