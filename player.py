BASE_STATS = {
    # combat stats
    "attack":           2,
    "crit":             1,
    "natural_armor":    1,
    "dodge":            0,
    "max_health":       10,
    "health":           10,
    # non-combat stats
    "has_eaten":        False,
    "gold":             0
}


class Player:

    name: str
    n_wins: int = 0
    n_gold: int = 0
    stats: dict = {}
    catch_phrase: str = "\"Shit... out of money again\""


    def __init__(self, name: str, adjustment_stats: dict):
        # set name 
        self.name = name
        self.setStats(adjustment_stats, BASE_STATS)
        #print(f"BASE STATS: {BASE_STATS}\nADJUSTMENT STATS: {adjustment_stats}")


    def setStats(self, adjustment_stats, base_stats=None):
        # set stats
        #print(f"base_stats = <{base_stats}>\nadjustment_stats: <{adjustment_stats}>")
        if base_stats:
            for stat in base_stats:
                self.stats[stat] = base_stats[stat]
                if stat in adjustment_stats:
                    self.stats[stat] += adjustment_stats[stat]
        else:
            for stat in self.stats:
                if stat in adjustment_stats:
                    # checks for a stat maximum and enforces it when adding stats. E.g. the "health" stat cannot
                    #   exceed the "max_health" stat.
                    if ("max_" + stat) in self.stats:
                        self.stats[stat] = min(self.stats["max_" + stat], self.stats[stat] + adjustment_stats[stat])
                    else:
                        self.stats[stat] += adjustment_stats[stat]


    def hasGold(self, cost: int):
        if self.stats["gold"] >= cost:
            print("Purchased item")
            return True
        else:
            print("You ain't got the cash")
            return False
    

    def playerHeal(self):
        current_health = self.stats["health"]
        # if player has eaten a hearty meal they restore 1/2 their hp, otherwise they restore 1/4th
        #   both restored values are rounded up. Hence dividing by 1.9 or 3.9 respectively
        if self.stats["has_eaten"]:
            self.setStats({"health": round(self.stats["max_health"] / 1.9)})
        else:
            self.setStats({"health": round(self.stats["max_health"] / 3.9)})
        self.stats["has_eaten"] = False

        #print(f"HEALED {self.stats["health"] - current_health} HEALTH AFTER RESTING")