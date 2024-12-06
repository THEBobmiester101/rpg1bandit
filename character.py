from gameBase import *
from time import sleep



class Character:

    name: str
    gold: int = 20

    def __init__(self, name: str):
        self.name = name


    def say(self, text: str):
        c = cstr(f"\"{text}\"", color.BLUE)
        print(f"{self.name}: {c}")


    def say_slow(self, text: str):
        print(f"{self.name}: {color.BLUE}", end = "")
        for w in text.split(' '):
            for c in w:
                print(c, end="", flush=True)
                sleep(0.01)
            print(' ', end="")
            sleep(0.05)
        print(color.END)


    def has_gold(self, cost: int) -> bool:
        return True if self.gold >= cost else False
