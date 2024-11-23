from fightable import Fightable
from gameBase import *
from items.itemOwner import ItemOwner



BASE_STATS = {
    # non-combat stats
    "has_eaten":        False,
    "gold":             20
}



class Player(Fightable, ItemOwner):

    name: str
    n_wins: int = 0
    n_gold_earned: int = 0
    stats: dict = {}
    catch_phrase: str = "Shit... out of money again"

    def __init__(self, name: str, adjustment_stats: dict):
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

        self.name = name
        self.addStats(adjustment_stats, BASE_STATS)
        #print(f"BASE STATS: {BASE_STATS}\nADJUSTMENT STATS: {adjustment_stats}")
        #print(f"PLAYER STATS ON __INIT__: {self.stats}")


    def addStats(self, adjustment_stats, base_stats = {}):
        #print(f"base_stats = <{base_stats}>\nadjustment_stats: <{adjustment_stats}>")
        for stat in base_stats:
            self.stats[stat] = base_stats[stat]

        for stat in adjustment_stats:
            if stat in self.stats:
                self.stats[stat] += adjustment_stats[stat]

        for stat in self.stats:
            if ("max_" + stat) in self.stats:
                self.stats[stat] = min(self.stats["max_" + stat], self.stats[stat])


    def has_gold(self, cost: int):
        return True if self.stats["gold"] >= cost else False
    

    def playerHeal(self):
        # if player has eaten a hearty meal they restore 1/2 their hp, otherwise they restore 1/4th
        #   both restored values are rounded up. Hence dividing by 1.9 or 3.9 respectively
        heal_amount = self.max_health / (1.9 if self.stats["has_eaten"] else 3.9)
        self.heal(round(heal_amount))
        self.stats["has_eaten"] = False

        #print(f"HEALED {self.stats["health"] - current_health} HEALTH AFTER RESTING")

    
    def say(self, text: str):
        c = cstr(f"\"{text}\"", color.BLUE)
        print(f"{self.name}: {c}")


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
