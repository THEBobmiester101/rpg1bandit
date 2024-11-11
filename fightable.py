from abc import ABC
from random import randint



class Fightable(ABC):

    max_health: int
    health: int
    attack: int
    crit: int
    natural_armor: int
    dodge: int


    def __init__(self, 
                 max_health, 
                 health = -1, 
                 attack = 0, 
                 crit = 0, 
                 natural_armor = 0, 
                 dodge = 0):
        
        self.max_health    = max_health
        self.health        = max_health if health < 0 else health
        self.attack        = attack
        self.crit          = crit
        self.natural_armor = natural_armor
        self.dodge         = dodge


    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)


    # return damage amount actually taken
    def take_damage(self, amount) -> int:
        amount = max(amount - self.natural_armor - self.dodge, 0)
        self.health = max(self.health - amount, 0)
        return amount


    # return damage amount applied to opponent
    def strike(self, opponent) -> int:
        damage = self.attack + (self.crit if randint(1, 4) == 4 else 0)
        return opponent.take_damage(damage)


    def dead(self) -> bool:
        return self.health < 1
