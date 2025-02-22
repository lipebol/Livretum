from os import getenv
import PySimpleGUI as sg
from utils.set import Set


class Notify:

    sg.theme(getenv('THEME'))
    def __init__(self):
        (self.size_x, self.loc_x, self.size_y, self.loc_y) = tuple(
            Set().screen((0.21961932650073207, 0.13020833333333334))
        )
        self.close_button = sg.Button(
            '', image_data=self.closeBase64(), border_width=0, key='Exit',
            button_color=(sg.theme_background_color())
        )

    
    def noNet(self):
        self.noNetWindow = sg.Window(
            getenv('NAME'), layout=[
                [sg.Column([[self.close_button]], justification='right')],
                [
                    sg.Column(
                        [[sg.Text('[:/] sem Internet.', font=getenv('DEFAULT_FONT'))]], 
                        justification=getenv('DEFAULT_JUSTIFICATION')
                    )
                ],
                [sg.Text('')],
            ],
            size=(self.size_x, self.size_y), resizable=True, grab_anywhere=True, 
            alpha_channel=.9, no_titlebar=True, location=(self.loc_x, self.loc_y)
        )

        while True:
            event, values = self.noNetWindow.read()
            if event == 'Exit':
                self.noNetWindow.Hide()
                break

    
    def closeBase64(self):
        return b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIf\
        AhkiAAAAAlwSFlzAAAAsQAAALEBxi1JjQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXB\
        lLm9yZ5vuPBoAAANJSURBVEiJtZXfa1tlGMc/z0lYVqXghTA3KP2xZlvdSjo7+yMNySpn2\
        hVBL0R2Mbx1Yv8dNxDEOztvh8wyZVsz2zWJztaatDVpShesVtiF9GJJ6XkfL056evJLg7A\
        XDueF9znfz/N9n/c8L7zgIe0EreSeXjCWRFT1BAYUsxtAlofOd2f/N2CxVOroeB6cQfVj1\
        JxGFQVQRVUBBdVNFb2195J8NtnbW24bsFrYjTqqt1HtcoUV1H2aQFB0Wxy5NhzpXarXshr\
        Ei399aJD7gnQhAiII7tud475F3Pzc9W4N6INMtvjBvzpYLTyLquh90JB6Gfuz/08nZXFk0\
        u/Ec7BYKnVgyW1EQuBmuP7bZl32jU6yuQ2/k+Ma0Nl8Ph9qAHQ6nTOIdB2KrG8U+Wr2G76\
        dm28JuXPnHl98+TW/ZmsgPX/vB2YaAILc8IucO9dPIj7K49Qyd5tA7s49JLmQ4XIiyuDgQ\
        G1N1LpRA8g93buASF+9iG3HSMRHWaqDzN1LMp9MkYiP8f577zQpPP1PstuvAwQBVCTiOVF\
        QOZrbdoyDA4eFxR8RQNXw6Ic08fgo7159i2q5EVW0Whu37iYC5IIAKCfFBTWFTE0lCAYDz\
        CdTGOMQm3iT6elJUK2LPYIY5JTnwLJQo+IFNIOIWFiWWzKxAghSs14PscRSD4AG/hAxqC/\
        A/+F33y+w+PgJ0fFLqBpvu65OJVpDlB0PYILWijiKCA2Q+Qcp0plfGB97g7ftCRT1tkuB6\
        RYQDTgrHuD8yVA29/vzPErYD3mYzLCUXmF05CK2Pe7tuW3HXHgyBc0hheEzPWveMQUQ5HO\
        qx0xEKBRLpDOrjIwMceXKRMN/YNsxJqKXWEots7ZRrF+/eaRbHVtberx8rLKuaHf1nFEob\
        HO6r8vrO81608b6JmfP9uLrXVsvszcQDocrNQCAtZ39YdQ8UrTjEKJ1za1lA3RjyxhzOXL\
        mtdShZk27Hjh17Cex5CNByv7t8je3xqZXnSNlRK/7xRscHI7cn/tj4phZRXvadLLlYK4N9\
        b2artdqeWXm8xo66Kh8qqKfoNrfFGI0D+ZW6OCVm+GwVJrptHXpr+5UBoKOuaiiJwwGUXa\
        Noz8P9nSutfP9Cx3/AEm78nl/zEWGAAAAAElFTkSuQmCC'