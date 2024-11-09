BASE_STATS = {
    "attack":           2,
    "crit":             1,
    "natural_armor":    1,
    "dodge":            0,
    "health":           10,
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
        
        # set stats
        for stat in BASE_STATS:
            self.stats[stat] = BASE_STATS[stat]
            if stat in adjustment_stats:
                self.stats[stat] += adjustment_stats[stat]


    def hasGold(self, cost: int):
        if self.stats["gold"] >= cost:
            print("Purchased item")
            return True
        else:
            print("You ain't got the cash")
            return False
        
    
