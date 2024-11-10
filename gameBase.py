from abc import ABC



class GameBase(ABC):

    @staticmethod
    def get_number_input(i_from: int, i_to: int) -> int:
        n = i_from - 1
        while n < i_from or n > i_to:
            try:
                n = int(input(f"(Enter {i_from}-{i_to}) > "))
            except:
                pass        
        return n

    @staticmethod
    def get_input_option(options: list) -> int:
        i = 1
        for opt in options:
            print(f"({i}) {opt}")
            i += 1

        return GameBase.get_number_input(1, options.__len__())
