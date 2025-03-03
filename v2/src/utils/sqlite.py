from ast import literal_eval
from os import getenv
import sqlite3


class SQLite:

    def __init__(self, default_dir: str) -> None:
        self.__sqlite_conn = sqlite3.connect(f'{default_dir}/livretum.db')
        self.__sqlite_cursor = self.__sqlite_conn.cursor()

    def launch(self):
        try:
            for command in literal_eval(getenv('DB_INIT')):
                self.__sqlite_cursor.execute(command)
            return True
        except Exception as error:
            print(error)
            return False

    def new_user(self, user: str) -> list:
        try:
            return self.dql('select_user_by_id', (self.dml('insert_user', (user,)),))[0]
        except Exception as error:
            print(error)

    def ddl(self, name: str) -> object:
        try:
            return self.__sqlite_cursor.execute(literal_eval(getenv('DDL')).get(name))
        except Exception as error:
            print(error)

    def dml(self, name: str, args: tuple) -> int:
        try:
            self.__sqlite_cursor.execute(literal_eval(getenv('DML')).get(name), args)
            self.__sqlite_conn.commit()
            return self.__sqlite_cursor.lastrowid
        except Exception as error:
            print(error)
            return False

    def dql(self, name: str, args=None) -> list:
        try:
            return self.__sqlite_cursor.execute(literal_eval(getenv('DQL')).get(name), args).fetchall()
        except Exception as error:
            print(error)
            return False