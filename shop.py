from gameBase import GameBase
from player import Player
from buyable import *



class Shop:

    buyables: dict = {}

    
    def __init__(self):
        self.buyables = {
            Service("A hearty meal",                     3 ):          100,
            Service("Gamble",                            10, gamble): -1,
            Service("Basic combat training",             15):          2,
            Service("Services of a skilled weaponsmith", 40):          2,
            Service("Services of a skilled tanner",      50):          2,
            Item(   "Magic Shop: ring of the fleet fox", 65):          1,
            Item(   "Magic Shop: vicious ring",          80):          1,
            Service("Nothin' else",                      0 ):         -.1
        }


    def loop(self, game: GameBase, player: Player) -> bool:
        self.buyables = dict(sorted(
            self.buyables.items(), key = lambda x: abs(x[1]), reverse = True))

        print(f"What would you like to buy? (You have {player.stats['gold']} gold)\n")

        for i, (buyable, quantity) in enumerate(self.buyables.items()):
            if quantity > 0:
                print(f"({i+1}) {buyable.name: <40} {buyable.cost: >10} gold {quantity: >10} pcs")
            elif quantity < 0:
                print(f"({i+1}) {buyable.name: <40} {buyable.cost: >10} gold")

        i = GameBase.get_number_input(1, self.buyables.items().__len__()) - 1
        buyable = list(self.buyables.keys())[i]

        if buyable.name == "Nothin' else":
            return False
        
        if player.has_gold(buyable.cost):
            player.stats["gold"] -= buyable.cost
            if self.buyables[buyable] > 0:
                self.buyables[buyable] -= 1
            if buyable is Item:
                player.items.append(buyable)
            print(f"Purchased: {buyable.name}")
            buyable.immediate(player, buyable.cost)
            game.end_day_script.append(f"Bought: {buyable.name}")
            
        else:
            print(f"Sorry pal, you ain't got the cash")

        return True
    