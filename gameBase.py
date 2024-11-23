from abc import ABC
from random import randint
import os



class color:
    DARK_CYAN   = '\033[36m'
    DARK_WHITE  = '\033[37m'
    GRAY        = '\033[90m'
    RED         = '\033[91m'
    GREEN       = '\033[92m'
    YELLOW      = '\033[93m'
    BLUE        = '\033[94m'
    MAGENTA     = '\033[95m'
    CYAN        = '\033[96m'
    WHITE       = '\033[97m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'
    END         = '\033[0m'
    ITALIC      = '\033[3m'



def cstr(text: str, col: color):
    return f"{col}{text}{color.END}"


def cprint(text: str, col: color):
    print(cstr(text, col))



class GameBase(ABC):

    day_events_list = []


    @staticmethod
    def get_number_input(i_from: int, i_to: int) -> int:
        n = i_from - 1
        while n < i_from or n > i_to:
            try:
                n = int(input(cstr(f"(Enter {i_from}-{i_to}) > ", color.GRAY)))
            except:
                pass
        os.system('cls')
        return n


    @staticmethod
    def get_input_option(options: list) -> int:
        for i, opt in enumerate(options):
            print(cstr(f"({i+1})", color.GRAY), opt)

        return GameBase.get_number_input(1, options.__len__())
