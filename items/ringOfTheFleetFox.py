from .item import Item



class RingOfTheFleetFox(Item):

    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            "A fleet fox, but poor fella seemingly still got turned into a ring...",
            {
                'add_item': self.__add,
                'remove_item': self.__remove
            }
        )


    def __add(self, player):
        player.dodge += 1


    def __remove(self, player):
        player.dodge -= 1
