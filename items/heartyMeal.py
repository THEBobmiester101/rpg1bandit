from .item import Item
from gameBase import *



class HeartyMeal(Item):

    def __init__(self):
        super().__init__(
            "A hearty meal",
            "Consistent taste, consistent price, consistently ...a hearty meal",
            {
                'add_item': self.__add,
                'end_day': self.__end_day
            }
        )


    def __add(self, player):
        player.say("Hmm ...with a full stomach tonight's sleep sure will be good")


    def __end_day(self, player):
        player.heal(round(player.max_health / 1.9))
        self.used_up = True
