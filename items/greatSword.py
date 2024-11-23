from .item import Item
from gameBase import *



class GreatSword(Item):

    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            "The worryingly bloodthirsty great sword",
            {
                'add_item': self.__add,
                'remove_item': self.__remove,
                'strike': self.__strike
            }
        )

    
    def __add(self, player):
        player.attack += 2
        print(cstr(f"\"Feed me... {cstr('blood', color.RED)}...\"", color.ITALIC))
        print("You feel compelled to feed the greatsword blood")

    
    def __remove(self, player):
        player.attack -= 2


    def __strike(self, player, opponent):
        print(cstr(f"\"delicious {cstr('blood', color.RED)}...\"", color.ITALIC))
        return opponent
