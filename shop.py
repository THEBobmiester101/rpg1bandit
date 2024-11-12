from gameBase import *
from player import Player
from buyable import *



class Shop:

    stock: dict = {}

    
    def __init__(self):
        self.stock = {
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
        print("What would you like to buy?", 
              f"(You have {cstr(player.stats['gold'], colors.YELLOW)} gold)\n")
        
        buyable = self.__select()
        if buyable.name == "Nothin' else":
            return False
        
        self.__sell(game, player, buyable)
        return True
    

    def __select(self) -> Buyable:
        options = []
        options_buyable = []
        for i, (buyable, quantity) in enumerate(self.stock.items()):
            if quantity == 0:
                continue
            s = f"{buyable.name: <40} "
            if buyable.cost != 0:
                s += f"{cstr(buyable.cost, colors.YELLOW): >20} gold "
            if quantity > 0:
                s += f"{cstr(quantity, colors.MAGENTA): >20} pcs "
            options.append(s)
            options_buyable.append(buyable)

        return options_buyable[GameBase.get_input_option(options) - 1]
    

    def __sell(self, game: GameBase, player: Player, buyable: Buyable):
        if player.has_gold(buyable.cost):
            self.stock[buyable] -= 1 if self.stock[buyable] > 0 else 0
            player.stats["gold"] -= buyable.cost
            if buyable is Item:
                player.items.append(buyable)
            buyable.immediate(player, buyable.cost)
            print(f"Purchased: {buyable.name}")
            game.end_day_script.append(f"Bought: {buyable.name}")
            
        else:
            print(f"Sorry pal, you ain't got the cash")
