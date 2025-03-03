from os import getenv, listdir
from os.path import expanduser
from requests import get
from utils.sqlite import SQLite


class Check:

    def connection(self):
        try:
            return get(getenv('URL_GOOGLE'))
        except Exception:
            return False

    def default_dir(self):
        return getenv('DEFAULT_DIR') % expanduser('~')

    def key(self):
        return '.ps.key' in listdir(self.default_dir())

    def db(self):
        return 'livretum.db' in listdir(self.default_dir())

    def username(self, username: str) -> list:
        self.__user = SQLite(self.default_dir()).dql('select_user_by_name', (username,))
        return self.__user[0] if self.__user != [] else SQLite(self.default_dir()).new_user(username)