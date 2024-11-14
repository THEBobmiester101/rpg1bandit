from fightable import Fightable
from gameBase import *



BASE_STATS = {
    # non-combat stats
    "has_eaten":        False,
    "gold":             20
}



class Player(Fightable):

    name: str
    n_wins: int = 0
    n_gold_earned: int = 0
    stats: dict = {}
    catch_phrase: str = "Shit... out of money again"
    items: list = []


    def __init__(self, name: str, adjustment_stats: dict):
        super(Player, self).__init__(
            max_health    = 10,
            health        = 10,
            attack        = 2,
            crit          = 1,
            natural_armor = 1,
            dodge         = 0
        )
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
        c = cstr(f"\"{text}\"", colors.BLUE)
        print(f"{self.name}: {c}")
