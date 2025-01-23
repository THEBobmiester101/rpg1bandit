from .item import Item
from gameBase import *



class PotionToughness(Item):

    def __init__(self):
        super().__init__(
            "Lesser Potion of Toughness",
            "Toughens your skin",
            {
                'add_item': self.__add,
                'remove_item': self.__remove,
                'end_day': self.__end_day
            }
        )


    def __add(self, player):
        #player.say("My skin feels like wood")
        player.say("Ever since I understood the weakness of my flesh I craved the certainty of steel")
        player.natural_armor += 2


    def __remove(self, player):
        #player.say("(potion wears off) My skin feels squishy again.")
        player.say("(potion wears off) The weakness of my flesh disgusts me.")
        player.natural_armor -= 2


    def __end_day(self, player):
        player.heal(round(player.max_health / 1.9))
        self.used_up = True
