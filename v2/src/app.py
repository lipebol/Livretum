from dotenv import load_dotenv
from PySimpleGUI import theme, WIN_CLOSED
from utils.check import Check
from utils.layout import Layout
from utils.notify import Notify
from utils.set import Set


class App:

    load_dotenv()
    theme('DarkGrey11')
    def __init__(self):
        self.layout = Layout(Set().logo(), Set().icon())


    def user(self) -> tuple:
        try:
            self.userWindow = self.layout.user(Set().screen((0.36603221083455345, 0.46875)))
            while True:
                event, values = self.userWindow.read()
                if event == WIN_CLOSED:
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


    def bookcase(self, user: tuple) -> str:
        try:
            self.bookcaseWindow = self.layout.bookcase(
                Set().screen((0.541727672035139, 0.5989583333333334)), 
                Set().bookcase(user)
            )
            while True:
                event, values = self.bookcaseWindow.read()
                if event == WIN_CLOSED:
                    return 'Exit'
                    break
                if event == 'Novo Livro':
                    return 'Reload'
        except Exception as error:
            print(error)
            return 'Error'


    def main(self) -> None:
        try:
            if not Check().connection():
                Notify().noNet()
            else:
                if Set().dir():
                    self.mainWindow = self.layout.main(Set().screen((0.36603221083455345, 0.390625)))
                    while True:
                        event, values = self.mainWindow.read()
                        if event == WIN_CLOSED:
                            break
                        if event == 'Minha Estante':
                            self.mainWindow.Hide()
                            self.__user = self.user()
                            if self.__user not in ('Error', 'Exit'):
                                while self.bookcase(self.__user) == 'Reload':
                                    continue
                        self.mainWindow.UnHide()
        except Exception as error:
            print(error)

if __name__ == '__main__':
    App().main()
        