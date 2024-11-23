from .item import Item



class ViciousRing(Item):

    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            "A ring, and a vicious one at that",
            {
                'add_item': self.__add,
                'remove_item': self.__remove
            }
        )


    def __add(self, player):
        player.attack += 1
        player.crit += 1
    

    def __remove(self, player):
        player.attack -= 1
        player.crit -= 1
