from .item import Item



class Shield(Item):

    __hits: int = 3

    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            "A shield that can reduce the damage of 3 hits before breaking",
            {
                'add_item': self.__add,
                'remove_item': self.__remove,
                'take_damage': self.__take_damage
            }
        )


    def __add(self, player):
        player.say("Oho now that's one beautiful shield")

    
    def __remove(self, player):
        player.say("It really was a good shield")
    

    def __take_damage(self, player, amount):
        self.__hits -= 1
        match self.__hits:
            case 2: 
                player.say("This but a scratch on my shiny shield")
            case 1: 
                player.say("Seems my shield has a few cracks")
            case 0: 
                player.say("Welp, there goes the shield")
                self.used_up = True
        return amount - 1
