from os import getenv
from requests import get
from utils.notify import Notify


class Check:

    def connection(self):
        try:
            return get(getenv('URL_GOOGLE'))
        except Exception:
            Notify().noNet()
            exit()