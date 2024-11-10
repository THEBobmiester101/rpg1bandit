from typing import Callable
from abc import ABC



def unimplemented():
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
