from dotenv import load_dotenv
from os import getenv
from platform import system
from subprocess import run, PIPE


class Set:

    load_dotenv()
    def screen(self, window_sizes: list):
        return tuple(self.calc(self.exec(getenv(f'{system()}_SCREEN')), window_sizes))

    def calc(self, screen_sizes: int, window_sizes: float):
        for screen_size, window_size in zip(screen_sizes, window_sizes):
            yield int(screen_size * window_size)
            yield (screen_size - int(screen_size * window_size)) // 2

    def exec(self, commands: str) -> list:
        return [
            int(size.split()[1]) if getenv('NEWLINE') in size else int(size) for size in [
                run(
                    command, shell=True, stdout=PIPE, text=True
                ).stdout.strip() for command in commands.split(getenv('SEPARATOR'))
            ]
        ]
