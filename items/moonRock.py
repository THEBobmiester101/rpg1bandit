from .item import Item
from gameBase import *



class MoonRock(Item):

    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            "A chunk of rock. It matches the phase of the moon.",
            {
                'add_item': self.__add,
                'remove_item': self.__remove,
                'strike': self.__strike
            }
        )

    
    def __add(self, player):
        print(cstr(f"\"Feed me... {cstr('blood', color.RED)}...\"", color.ITALIC))
        print("You feel compelled to feed the moon rock")

    
    def __remove(self, player):
        pass


    def __strike(self, player, opponent):
        print(cstr(f"\"delicious {cstr('blood', color.RED)}...\"", color.ITALIC))
        return opponent
