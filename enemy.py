from typing import Tuple
from fightable import Fightable
from random import randint
from gameBase import *



class Enemy(Fightable):

    attack: int
    crit: int
    assessment: str
    gold: int


    def __init__(self):
        super().__init__(
            max_health    = 30,
            health        = randint(1, 10) * 3,
            attack        = randint(1, 4),
            crit          = randint(1, 3),
            natural_armor = randint(0, 2),
            dodge         = randint(-2, 3)
        )

        self.assessment, self.gold = self.__assess()


    def __assess(self) -> tuple[str, int]:
        """ An enemy's worth is determined by its other stats. Each tier is generally worth (tier^2 - 1)/2 gold. 
        Damage is not halved, because it makes the other stats much more effective.
        """
        statements = []
        gold = 0

        damage = self.attack * 2 + self.crit
        if damage > 9:
            statements.append("very dangerous")
            gold += 15
        elif damage > 6:
            statements.append("dangerous")
            gold += 8
        elif damage > 3:
            statements.append("mildly dangerous")
            gold += 3
        else:
            statements.append("not very dangerous")
            # not worth gold

        toughness = self.natural_armor * 4 + self.health
        if toughness > 30:
            statements.append("very tough")
            gold += 7
        elif toughness > 20:
            statements.append("tough")
            gold += 4
        elif toughness > 10:
            statements.append("somewhat tough")
            gold += 1
        else:
            statements.append("not very tough")
            # not worth gold

        swiftness = self.dodge
        if swiftness > 2:
            statements.append("very agile")
            gold += 7
        elif swiftness > 0:
            statements.append("agile")
            gold += 4
        elif swiftness > -1:
            # asessing_statements.append("of normal speed")
            # not sure what a good way to say "average speed" is, probably best to not say anything
            gold += 1
        else:
            statements.append("unusually slow")
            # not worth gold

        gold = max(gold, 1) # each job is worth at least 1 gold
        return ", ".join(statements), gold


    def take_damage(self, amount):
        amount = super().take_damage(amount)

        if amount > round(self.max_health / 1.9):
            cprint("Dealt massive damage", color.GREEN)
        elif self.dead():
            cprint("A felling strike", color.GREEN)
        elif amount > 4:
            cprint("Strong attack", color.GREEN)
        elif amount > 1:
            cprint("Dealt some damage", color.GREEN)
        elif amount == 1:
            cprint("Barely hurt them...", color.GREEN)
        else:
            cprint("Dealt no damage", color.GREEN)

        return amount
