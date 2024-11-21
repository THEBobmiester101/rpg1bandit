from typing import Callable
from abc import ABC
from random import randint
from gameBase import *



def unimplemented(real_parameter, im_with_real):
    print("Item not implemented yet")
    


def gamble(player, bet_amount):
    gold_won = randint(0, 2) * (bet_amount - 1)
    player.stats["gold"] += gold_won
    player.n_gold_earned += gold_won - bet_amount
    print(f"Got back {gold_won} gold")
    

def basicCombatTraining(player, _):
    player.dodge += 1
    player.crit += 1
    

def weaponSmith(player, _):
    player.attack += 1
    

def armorSmith(player, _):
    player.natural_armor += 1
    

def magicRingFleet(player, _):
    player.dodge += 1
    

def magicRingVicious(player, _):
    player.attack += 1
    player.crit += 1
    

def magicGreatSword(player, _):
    player.attack += 2
    print(f"\"Feed me... {cstr('blood...', colors.RED)}\"")
    print("You feel compelled to feed the greatsword blood")


class Buyable(ABC):

    name: str
    cost: int
    immediate: Callable

    def __init__(self, name: str, cost: int, immediate = unimplemented):
        self.name = name
        self.cost = cost
        self.immediate = immediate



class Service(Buyable):
    pass
        


class Item(Buyable):

    per_round: Callable

    def __init__(self, name: str, cost: int, immediate = unimplemented, per_round = unimplemented):
        super(Item, self).__init__(name, cost, immediate)
        self.per_round = per_round
