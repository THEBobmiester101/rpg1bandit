from article import Item



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
    items: list = []


    def __init__(self, name: str, adjustment_stats: dict):
        self.name = name
        self.setStats(BASE_STATS, adjustment_stats)
        #print(f"BASE STATS: {BASE_STATS}\nADJUSTMENT STATS: {adjustment_stats}")


    def setStats(self, base_stats, adjustment_stats = {}):
        #print(f"base_stats = <{base_stats}>\nadjustment_stats: <{adjustment_stats}>")
        for stat in base_stats:
            self.stats[stat] = base_stats[stat]
            if stat in adjustment_stats:
                self.stats[stat] += adjustment_stats[stat]

        for stat in self.stats:
            if ("max_" + stat) in self.stats:
                self.stats[stat] = min(self.stats["max_" + stat], self.stats[stat])


    def has_gold(self, cost: int):
        return True if self.stats["gold"] >= cost else False
    

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
