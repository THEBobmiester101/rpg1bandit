from gameBase import *
from player import Player
from buyable import *

from items.shield import Shield
from items.ringOfTheFleetFox import RingOfTheFleetFox
from items.viciousRing import ViciousRing
from items.greatSword import GreatSword



class Shop:

    stock: dict[Buyable, int] = {}

    
    def __init__(self):
        self.stock = {
            Service("A hearty meal",                             3): 100,
            Gamble("Gamble",                                    10):  -1,
            CombatTraining("Basic combat training",             15):   2,
            WeaponSmith("Services of a skilled weaponsmith",    40):   2,
            ArmorSmith("Services of a skilled tanner",          50):   2,
            BuyableItem(Shield(),                               25):   3,
            BuyableItem(RingOfTheFleetFox(),                    65):   1,
            BuyableItem(ViciousRing(),                          80):   1,
            BuyableItem(GreatSword(),                          120):   1,
            Service("Nothin' else",                              0):  -1
        }


    def loop(self, game: GameBase, player: Player) -> bool:
        print("What would you like to buy?", 
              f"(You have {cstr(player.stats['gold'], color.YELLOW)} gold)\n")
        
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
            if buyable.price != 0:
                s += f"{cstr(buyable.price, color.YELLOW): >20} gold "
            if quantity > 0:
                s += f"{cstr(quantity, color.MAGENTA): >20} pcs "
            options.append(s)
            options_buyable.append(buyable)

        return options_buyable[GameBase.get_input_option(options) - 1]
    

    def __sell(self, game: GameBase, player: Player, buyable: Buyable):
        if player.has_gold(buyable.price):
            self.stock[buyable] -= 1 if self.stock[buyable] > 0 else 0
            player.stats["gold"] -= buyable.price
            print(f"Purchased: {buyable.name}")
            buyable.on_bought(player)
            game.day_events_list.append(f"Bought: {buyable.name}")
        else:
            print(f"Sorry pal, you ain't got the cash")
