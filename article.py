from typing import Callable
from abc import ABC
from random import randint



def unimplemented(real_parameter, im_with_real):
    print("Item not implemented yet")
    pass


def gamble(player, bet_amount):
    gold_won = randint(0, 2) * (bet_amount - 1)
    player.stats["gold"] += gold_won
    player.n_gold_earned += gold_won - bet_amount
    print(f"Got back {gold_won} gold")
    pass



class Article(ABC):

    name: str
    cost: int
    immediate: Callable

    def __init__(self, name: str, cost: int, immediate = unimplemented):
        self.name = name
        self.cost = cost
        self.immediate = immediate



class ImmediateArticle(Article):
    pass
        


class Item(Article):

    per_round: Callable

    def __init__(self, name: str, cost: int, immediate = unimplemented, per_round = unimplemented):
        super(Item, self).__init__(name, cost, immediate)
        self.per_round = per_round
