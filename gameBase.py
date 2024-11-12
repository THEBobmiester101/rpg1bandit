from abc import ABC
from random import randint



class colors:
    GRAY    = '\033[90m'
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'


def cstr(text: str, col: colors):
    return f"{col}{text}{colors.WHITE}"


def cprint(text: str, col: colors):
    print(cstr(text, col))



class GameBase(ABC):

    end_day_script = []


    @staticmethod
    def get_number_input(i_from: int, i_to: int) -> int:
        n = i_from - 1
        while n < i_from or n > i_to:
            try:
                n = int(input(cstr(f"(Enter {i_from}-{i_to}) > ", colors.GRAY)))
            except:
                pass        
        return n


    @staticmethod
    def get_input_option(options: list) -> int:
        for i, opt in enumerate(options):
            print(cstr(f"({i+1})", colors.GRAY), opt)

        return GameBase.get_number_input(1, options.__len__())
