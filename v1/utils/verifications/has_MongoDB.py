import PySimpleGUI as sg
import os
from utils.verifications.path_User import pathUser
from utils.window.screen import screen

def hasMongoDB():

    sg.theme('DarkGrey11')

    x, y = 0.3367496339677892, 0.234375
    size_x, size_y, loc_x, loc_y = screen(x, y)
    directory, files = pathUser()

    buttonclose = sg.Button('', image_data=buttonclose_base64, 
            button_color=
            (
                sg.theme_background_color(),
            ),
            border_width=0, key='Exit')

    message = sg.Text(
        "[!] Livretum precisa do MongoDB.\n\n    Já possui um banco criado?", 
        font='Courier'
    )
    buttonYes = sg.Button("Sim", font='Courier')
    buttonNo = sg.Button("Não", font='Courier')
   
    layout_hasMongoDB = [
        [sg.Column([[buttonclose]], justification='right')],
        [sg.Column([[message]], justification='center')],
        [sg.Column([[buttonYes]], justification='center'), sg.Column([[buttonNo]])],
    ]

    window_hasMongoDB = sg.Window( 
        "Livretum",
        layout=layout_hasMongoDB, 
        size=(size_x, size_y),
        resizable=True,
        grab_anywhere=True,
        alpha_channel=.9, 
        no_titlebar=True,
        location=(loc_x, loc_y)
    )

    while True:
        event, values = window_hasMongoDB.read()
        if event:
            window_hasMongoDB.Hide()
            if event != "Sim":
                if ".ps.key" in files:
                    os.remove(f"{directory}/.ps.key")
                if os.path.isdir(directory):
                    os.rmdir(directory)
                if event == "Exit":
                    return "Exit"
                if event == "Não":
                    return "No"
                break
            else:
                return "Yes"
                break


# Button_Close Image
buttonclose_base64 = b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAAsQAAALEBxi1JjQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANJSURBVEiJtZXfa1tlGMc/z0lYVqXghTA3KP2xZlvdSjo7+yMNySpn2hVBL0R2Mbx1Yv8dNxDEOztvh8wyZVsz2zWJztaatDVpShesVtiF9GJJ6XkfL056evJLg7AXDueF9znfz/N9n/c8L7zgIe0EreSeXjCWRFT1BAYUsxtAlofOd2f/N2CxVOroeB6cQfVj1JxGFQVQRVUBBdVNFb2195J8NtnbW24bsFrYjTqqt1HtcoUV1H2aQFB0Wxy5NhzpXarXshrEi399aJD7gnQhAiII7tud475F3Pzc9W4N6INMtvjBvzpYLTyLquh90JB6Gfuz/08nZXFk0u/Ec7BYKnVgyW1EQuBmuP7bZl32jU6yuQ2/k+Ma0Nl8Ph9qAHQ6nTOIdB2KrG8U+Wr2G76dm28JuXPnHl98+TW/ZmsgPX/vB2YaAILc8IucO9dPIj7K49Qyd5tA7s49JLmQ4XIiyuDgQG1N1LpRA8g93buASF+9iG3HSMRHWaqDzN1LMp9MkYiP8f577zQpPP1PstuvAwQBVCTiOVFQOZrbdoyDA4eFxR8RQNXw6Ic08fgo7159i2q5EVW0Whu37iYC5IIAKCfFBTWFTE0lCAYDzCdTGOMQm3iT6elJUK2LPYIY5JTnwLJQo+IFNIOIWFiWWzKxAghSs14PscRSD4AG/hAxqC/A/+F33y+w+PgJ0fFLqBpvu65OJVpDlB0PYILWijiKCA2Q+Qcp0plfGB97g7ftCRT1tkuB6RYQDTgrHuD8yVA29/vzPErYD3mYzLCUXmF05CK2Pe7tuW3HXHgyBc0hheEzPWveMQUQ5HOqx0xEKBRLpDOrjIwMceXKRMN/YNsxJqKXWEots7ZRrF+/eaRbHVtberx8rLKuaHf1nFEobHO6r8vrO81608b6JmfP9uLrXVsvszcQDocrNQCAtZ39YdQ8UrTjEKJ1za1lA3RjyxhzOXLmtdShZk27Hjh17Cex5CNByv7t8je3xqZXnSNlRK/7xRscHI7cn/tj4phZRXvadLLlYK4N9b2artdqeWXm8xo66Kh8qqKfoNrfFGI0D+ZW6OCVm+GwVJrptHXpr+5UBoKOuaiiJwwGUXaNoz8P9nSutfP9Cx3/AEm78nl/zEWGAAAAAElFTkSuQmCC'

