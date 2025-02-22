from cryptography.fernet import Fernet
from os import getenv, makedirs, chmod, listdir
from os.path import abspath, expanduser, isdir
from platform import system
from subprocess import run, PIPE


class Set:

    def __init__(self):
        self.default_dir = getenv('DEFAULT_DIR') % expanduser('~')
        self.system = system()

    def logo(self):
        return abspath(getenv('LOGO'))
        
    def icon(self):
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

    def dir(self):
        try:
            if not isdir(self.default_dir):
                makedirs(self.default_dir)
                if '.ps.key' not in listdir(self.default_dir):
                    with open(f'{self.default_dir}/.ps.key', 'wb') as key:
                        key.write(Fernet.generate_key())
            return True
        except Exception as error:
            print(error)
            return False
