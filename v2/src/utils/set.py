from ast import literal_eval
from cryptography.fernet import Fernet
from os import (getenv, makedirs, chmod)
from os.path import (abspath, isdir)
import pandas as pd
from platform import system
from PIL import Image
from requests import get
from subprocess import (run, PIPE)
from textwrap import TextWrapper
from utils.sqlite import SQLite


class Set:

    def __init__(self, Check: object) -> None:
        self.__check, self.system = Check, system()

    def __request(self, url: str, args=None, stream=None):
        try:
            self.data = get(url if stream else getenv(url) % args, stream=stream)
            return self.data.content if stream else self.data.json() if self.data.status_code == 200 else None
        except Exception as error:
            print(error)
            
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
                        f'{self.system}_SCREEN').split(getenv('SEPARATOR')
                    )
                ]
            ], window_sizes):
                yield int(screen_size * window_size)
                yield (screen_size - int(screen_size * window_size)) // 2

    def dir(self) -> bool:
        try:
            if not isdir(self.__check.default_dir()):
                for dir in [self.__check.default_dir(), self.__check.tmp_dir()]:
                    makedirs(dir)
                if not self.__check.key():
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

    def bookcase(self, user=None):
        try:
            if user:
                self.id, self.username = user
            return pd.DataFrame(
                SQLite(self.__check.default_dir()).dql('select_bookcase_by_id', (self.id,)),
                columns=literal_eval(getenv('BOOKCASE_COLUMNS'))
            )
        except Exception as error:
            print(error)

    def search(self, book: str|dict) -> list:
        def extract(book: dict):
            def image(links: dict):
                try:
                    content = self.__request(links.get('smallThumbnail'), stream=True)
                    if content:
                        with open(getenv('JPEG_IMAGE') % self.__check.tmp_dir(), 'wb') as img:
                            img.write(content)
                        img = Image.open(getenv('JPEG_IMAGE') % self.__check.tmp_dir())
                        if img:
                            if img.size[0] == 128 and img.size[1] >= 155:
                                return True if not img.save(
                                    getenv('PNG_IMAGE') % self.__check.tmp_dir()
                                ) else None                                
                except Exception as error:
                    print(f"{error} in image")
            try:
                info = book.get('volumeInfo')
                return {
                    'url': f'{book.get('selfLink')}?fields=volumeInfo',
                    'title': TextWrapper(width=42).fill(
                        text=info.get('title') if 'subtitle' not in info else f'{
                            info.get('title')}-{info.get('subtitle')}'
                    ),
                    'authors': TextWrapper(width=35).fill(
                        text=getenv('COMMA').join(info.get('authors')) if 'authors' in info else ''
                    ),
                    'id': {
                        'isbn_10' if len(value) == 10 else 'isbn_13' if len(value) == 13 else '': 
                        value for value in [dict.get('identifier') for dict in info.get('industryIdentifiers')]
                    } if 'industryIdentifiers' in info else '',
                    'image': getenv('PNG_IMAGE') % self.__check.tmp_dir() if 'imageLinks' in info 
                             and image(info.get('imageLinks')) else abspath(getenv('NO_IMAGE'))
                }
            except Exception as error:
                print(f"{error} in extract")
        try:
            self.data = self.__request(
                'API_GOOGLE_BOOKS', book).get('items') if type(book) == str else extract(book)
            return [self.data] if not self.data and type(book) == str else self.data
        except Exception as error:
            print(f"{error} in search")
        
        
    def acquired(self, id: str):
        try:
            self.book = self.bookcase().values.tolist()[int(id)-1]
            return SQLite(self.__check.default_dir()).dml(
                'update_acquired', ('S',self.book[2],self.book[3],self.id,)
            )
        except Exception as error:
            print(error)



