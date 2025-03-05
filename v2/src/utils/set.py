from ast import literal_eval
from cryptography.fernet import Fernet
from os import getenv, makedirs, chmod
from os.path import abspath, isdir
import pandas as pd
from platform import system
import PySimpleGUI as sg
from subprocess import run, PIPE
from utils.check import Check
from utils.sqlite import SQLite


class Set:

    def __init__(self) -> None:
        self.__check = Check()
        self.system = system()
        
    def logo(self) -> str:
        return abspath(getenv('LOGO'))
        
    def icon(self) -> str:
        return getenv(f'{self.system}_ICON')

    def screen(self, window_sizes: tuple) -> object:
        for screen_size, window_size in zip(
            [
                int(size.split()[1]) if getenv('NEWLINE') in size else int(size) for size in [
                    run(
                        command, shell=True, stdout=PIPE, text=True
                    ).stdout.strip() for command in getenv(
                        f'{self.system}_SCREEN').split(getenv('SEPARATOR'))
                ]
            ], window_sizes):
                yield int(screen_size * window_size)
                yield (screen_size - int(screen_size * window_size)) // 2

    def dir(self) -> bool:
        try:
            if not isdir(self.__check.default_dir()):
                makedirs(self.__check.default_dir())
                if '.ps.key' not in listdir(self.__check.default_dir()):
                    with open(f'{self.__check.default_dir()}/.ps.key', 'wb') as key:
                        key.write(Fernet.generate_key())
            return True
        except Exception as error:
            print(error)
            return False

    def db(self, username: str):
        try:
            self.__db = SQLite(self.__check.default_dir())
            if self.__db.launch():
                return self.__db.new_user(username)
        except Exception as error:
            print(error)
            return False

    def bookcase(self, user: tuple):
        try:
            self.id, self.username = user
            return pd.DataFrame(
                SQLite(self.__check.default_dir()).dql('select_bookcase_by_id', (self.id,)),
                columns=literal_eval(getenv('BOOKCASE_COLUMNS'))
            )
        except Exception as error:
            print(error)




