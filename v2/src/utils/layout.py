from os import getenv
from PySimpleGUI import (Button, Column, Image, InputText, Table, Text, Window)


class Layout:
    
    def __init__(self, logo, icon) -> None:
        self.logo, self.icon = logo, icon


    def main(self, screen: object) -> object:
        self.size_x, self.loc_x, self.size_y, self.loc_y = tuple(screen)
        return Window(
            getenv('NAME'), icon=self.icon, layout=[
                [Text('')],
                [
                    Column(
                        [[Image(filename=self.logo)]], 
                        justification=getenv('DEFAULT_JUSTIFICATION')
                    )
                ],
                [Text('')],
                [
                    Column(
                        [[Button('Minha Estante', font=getenv('DEFAULT_FONT'))]], 
                        justification=getenv('DEFAULT_JUSTIFICATION')
                    )
                ],
                [
                    Column(
                        [[Button('Recomendações', font=getenv('DEFAULT_FONT'), disabled=True)]], 
                        justification=getenv('DEFAULT_JUSTIFICATION')
                    )
                ],
                [Text('')]
            ], 
            size=(self.size_x, self.size_y), resizable=True, grab_anywhere=True, 
            alpha_channel=.9, location=(self.loc_x, self.loc_y)
        )


    def user(self, screen: object) -> object:
        self.size_x, self.loc_x, self.size_y, self.loc_y = tuple(screen)
        return Window(
            getenv('NAME'), icon=self.icon, layout=[ 
                [Text('')],
                [Column([[Image(filename=self.logo)]])],
                [Text('')],
                [Column([[Text('Quem é o dono da estante?',font=getenv('DEFAULT_FONT'))]])],
                [Column([[InputText('',key='user',size=(20),font=getenv('DEFAULT_FONT'),focus=True)]])],
                [Text('')],
                [Button('Enviar',font=getenv('DEFAULT_FONT'),bind_return_key=True)]
            ],
            size=(self.size_x, self.size_y), resizable=True, grab_anywhere=True, 
            alpha_channel=.9, element_justification='c', location=(self.loc_x, self.loc_y)
        )


    def bookcase(self, screen: object, table: object) -> object:
        self.size_x, self.loc_x, self.size_y, self.loc_y = tuple(screen)
        return Window(
            getenv('NAME'), icon=self.icon, layout=[
                [Text('')],
                [Column([[Image(filename=self.logo)]])],
                [Text('')],
                [Text('')],
                [Text('')],
                [Text('')],
                [Text('[!] Nenhum livro cadastrado.',font=getenv('DEFAULT_FONT'))],
                [Text('')],
                [Text('')],
                [Text('')],
                [Text('')],
                [Button('Novo Livro',font=getenv('DEFAULT_FONT'))]
            ] if table.values.tolist() == [] else [
                [Text('')],
                [Column([[Image(filename=self.logo)]])],
                [
                    Table(
                        values=table.values.tolist(),headings=table.columns.tolist(), 
                        auto_size_columns=True,font=getenv('DEFAULT_FONT'), 
                        justification=getenv('DEFAULT_JUSTIFICATION')
                    )
                ],
                [Text('')],
                [
                    Column([[Button('Novo Livro',font=getenv('DEFAULT_FONT'))]]), 
                    Column([[Button('Adquirido?',font=getenv('DEFAULT_FONT'))]])
                ]
            ], 
            size=(self.size_x, self.size_y), resizable=True, grab_anywhere=True, 
            alpha_channel=.9, element_justification='c', location=(self.loc_x, self.loc_y)
        )
    

    def statusAcquired(self, screen: object) -> object:
        self.size_x, self.loc_x, self.size_y, self.loc_y = tuple(screen)
        return Window(
            getenv('NAME'), icon=self.icon, layout=[
                [Text('')],
                [Column([[Text('Qual o "id" do livro?',font=getenv('DEFAULT_FONT'))]])],
                [Text('')],
                [Column([[InputText('',key='id',size=(15),font=getenv('DEFAULT_FONT'),focus=True)]])],
                [Text('')],
                [Button('Enviar',font=getenv('DEFAULT_FONT'),bind_return_key=True)]
            ],
            size=(self.size_x, self.size_y), resizable=True, grab_anywhere=True, 
            element_justification='c', location=(self.loc_x, self.loc_y)
        )

    
    def thisId(self, screen: object, book: list) -> object:
        self.size_x, self.loc_x, self.size_y, self.loc_y = tuple(screen)
        return Window(
            getenv('NAME'), icon=self.icon, layout=[
                [Text('')],
                [
                    Column([[Text('[!] Você adquiriu o livro abaixo:',font=getenv('DEFAULT_FONT'))]])
                ],
                [
                    Column([[Text(f'Título: {book[2]}',font=getenv('DEFAULT_FONT'))]])
                ],
                [
                    Column([[Text(f'Autor(es): {book[3]}',font=getenv('DEFAULT_FONT'))]])
                ],
                [Column([[Button('Confirmar',font=getenv('DEFAULT_FONT'))]])],
            ],
            size=(self.size_x, self.size_y), grab_anywhere=True, 
            element_justification='c', location=(self.loc_x, self.loc_y)
        )
