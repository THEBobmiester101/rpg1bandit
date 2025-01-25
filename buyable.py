from abc import ABC
from random import randint
from gameBase import *
from items.item import Item



class Buyable(ABC):

    name: str
    price: int

    def on_bought(self, player):
        pass



class BuyableItem(Buyable):
    
    item: Item

    def __init__(self, item: Item, price: int):
        self.item = item
        self.name = item.name
        self.price = price

    def on_bought(self, player):
        player.add_item(self.item)



class Service(Buyable):

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        


class Gamble(Service):

    def on_bought(self, player):
        gold_won = randint(0, 2) * (self.price - 1)
        player.gold += gold_won
        player.n_gold_earned += gold_won - self.price
        print(f"Got back {gold_won} gold")
    


class CombatTraining(Service):

    def on_bought(self, player):
        player.dodge += 1
        player.crit += 1



class WeaponSmith(Service):

    def on_bought(self, player):
        player.attack += 1



class ArmorSmith(Service):

    def on_bought(self, player):
        player.natural_armor += 1    
