from character import Character
from fightable import Fightable
from items.itemOwner import ItemOwner
from gameBase import *



class Player(Character, Fightable, ItemOwner):

    n_wins: int = 0
    n_gold_earned: int = 0
    stats: dict = {}
    catch_phrase: str = "Shit... out of money again"

    def __init__(self, name: str):
        Character.__init__(self, name)
        Fightable.__init__(
            self,
            max_health    = 10,
            health        = 10,
            attack        = 2,
            crit          = 1,
            natural_armor = 1,
            dodge         = 0
        )
        ItemOwner.__init__(self)


    @ItemOwner.item_callback
    def end_day(self):
        self.heal(round(self.max_health / 1.9))


    @ItemOwner.item_callback
    def take_damage(self, amount):
        amount = super().take_damage(amount)
        
        if amount > 4:
            self.say("I'm... about to pass out.")
            cprint("You can't take another hit like that", color.RED)
        elif amount > 1:
            cprint("Took a nasty wound. That hurt like hell", color.RED)
        elif amount == 1:
            cprint("Took a minor wound", color.RED)
        else:
            cprint("They couldn't manage to wound you", color.RED)

        return amount


    @ItemOwner.item_callback
    def strike(self, opponent):
        return super().strike(opponent)
    

    @ItemOwner.item_callback
    def assess_health(self):
        if self.health == self.max_health:
            self.say("Feeling in tip-top shape")
        elif self.health > (3/4*self.max_health):
            self.say("Not feeling my best, but not too shabby")
        elif self.health > (1/4*self.max_health):
            self.say("Feeling beat")
        elif self.health > (0/4*self.max_health):
            self.say("Feeling like I'm on death's door")
        return
