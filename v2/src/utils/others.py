from PySimpleGUI import WIN_CLOSED


class Others:

    def __init__(self, Set: object, Layout: object) -> None:
        self.__set, self.__layout = Set, Layout

    def statusAcquired(self) -> str:
        try:
            self.statusAcquiredWindow = self.__layout.statusAcquired(
                self.__set.screen((0.24890190336749635, 0.2734375))
            )
            while True:
                event, values = self.statusAcquiredWindow.read()
                if event == WIN_CLOSED:
                    return 'Exit'
                    break
                if event == 'Enviar':
                    if values['id'] and values['id'].isdigit():
                        if int(values['id']) <= len(self.__set.bookcase().values.tolist()):
                            if self.__set.bookcase().values.tolist()[int(values['id'])-1][-1] != 'S':
                                self.statusAcquiredWindow.Hide()
                                return self.thisId(values['id'])
                                break
        except Exception as error:
            print(error)
            return 'Error'


    def thisId(self, id: str) -> str:
        try:
            self.thisIdWindow = self.__layout.thisId(
                self.__set.screen((0.3953147877013177, 0.2734375)), 
                self.__set.bookcase().values.tolist()[int(id)-1]
            )
            while True:
                event, values = self.thisIdWindow.read()
                if event == WIN_CLOSED:
                    return 'Exit'
                    break
                if event == 'Confirmar':
                    self.thisIdWindow.Hide()
                    return self.__set.updateAcquired(id)
                    break
        except Exception as error:
            print(error)
            return 'Error'
