from PySimpleGUI import WIN_CLOSED

from time import sleep

class Others:

    def __init__(self, Set: object, Layout: object) -> None:
        self.__set, self.__layout = Set, Layout

    def search(self) -> str:
        def choose(book: dict):
            try:
                chooseWindow = self.__layout.search(
                    self.__set.screen((0.43923865300146414, 0.859375)),
                    self.__set.search(book)
                )
                while True:
                    event, values = chooseWindow.read()
                    if event == WIN_CLOSED:
                        return 'Exit'
                    if event == 'Sim':
                        return True
                    if event == 'Não':
                        chooseWindow.Hide()
                        return None 
            except Exception as error:
                print(f"{error} in 'Others.search.choose'")
        try:  
            self.searchWindow = self.__layout.search(
                self.__set.screen((0.29282576866764276, 0.46875))
            )
            while True:
                event, values = self.searchWindow.read()
                if event == WIN_CLOSED:
                    return 'Reload'
                if event == 'Pesquisar':
                    if values['book']:
                        for book in self.__set.search(values['book']):
                            if book:
                                if choose(book):
                                    break
                        print(book)
                            #print('não tem nada!')       
        except Exception as error:
            print(f"{error} in 'Others.search'")

    def acquired(self) -> str:
        def confirm(id: str) -> str:
            try:
                confirmWindow = self.__layout.acquired(
                    self.__set.screen((0.3953147877013177, 0.2734375)), 
                    self.__set.bookcase().values.tolist()[int(id)-1]
                )
                while True:
                    event, values = confirmWindow.read()
                    if event == WIN_CLOSED:
                        return None
                    if event == 'Confirmar':
                        confirmWindow.Hide()
                        return self.__set.acquired(id)
            except Exception as error:
                print(f"{error} in 'Others.acquired.confirm'")
        try:
            self.acquiredWindow = self.__layout.acquired(
                self.__set.screen((0.24890190336749635, 0.2734375))
            )
            while True:
                event, values = self.acquiredWindow.read()
                if event == WIN_CLOSED:
                    return None
                if event == 'Enviar':
                    if values['id'] and values['id'].isdigit():
                        if int(values['id']) <= len(self.__set.bookcase().values.tolist()):
                            if self.__set.bookcase().values.tolist()[int(values['id'])-1][-1] != 'S':
                                self.acquiredWindow.Hide()
                                return confirm(values['id'])
        except Exception as error:
            print(f"{error} in 'Others.acquired'")
