from gameBase import *
from player import Player
from shop import Shop
from fight import Fight
import os



LINE_BREAK = "----------------------------------"
GAME_OPTIONS = [
    "Find enemy to fight",
    "Rest and recover",
    "Visit shop",
    "Next day",
    "Quit"
]




class Game(GameBase):
    
    player: Player
    shop: Shop
    n_days: int = 0
    can_fight: bool = True
    can_rest: bool = True


    def __init__(self, console_line_height):
        player_name = input("Choose a name for your character: ")
        self.player = Player(player_name)
        self.shop = Shop()

        clear()
        self.__new_day()

    
    def __del__(self):
        self.__end_day()
        print(self.player.name + "\'s journey ends.")
        print(f"Reached day {self.n_days}, killed {self.player.n_wins}, earned {self.player.n_gold_earned} gold")


    def loop(self) -> bool:    
        print("What would you like to do?")
        match GameBase.get_input_option(GAME_OPTIONS):
            case 1:
                if self.can_fight:
                    self.can_rest = False
                    fight = Fight(self, 3)
                    while fight.loop(): 
                        pass
                    del fight
                else:
                    print("You're taking it easy today, remember?")

            case 2:
                if self.can_rest:
                    self.player.playerHeal()
                    self.can_fight, self.can_rest = False, False
                    self.day_events_list.append("Rested for most of the day")
                    print("Took most of the day to rest and recover")
                elif self.can_fight:
                    print("You can't rest on a day you got in a fight!")
                else:
                    print("You're already taking the day to rest!")

            case 3:
                print("\nWelcome to the shop.")
                while self.shop.loop(self, self.player):
                    print()
                print("See you 'round\n")

            case 4:
                self.__end_day()
                self.__new_day()

            case 5:
                return False
        
        print()
        return True


    def __new_day(self):
        self.n_days += 1

        print(LINE_BREAK)
        print(f"Day {self.n_days} begins")
        if self.n_days > 1:
            self.player.assess_health()
        else:
            self.player.say(self.player.catch_phrase)
            #self.player.say_slow(self.player.catch_phrase)
        print(LINE_BREAK)


    def __end_day(self):
        self.player.end_day()
        self.can_fight, self.can_rest = True, True

        print(LINE_BREAK)
        print(f"Day {self.n_days} ends")
        if len(self.day_events_list) > 0:
            print("Summary:")
            print("- " + "\n- ".join(self.day_events_list))

        self.day_events_list.clear()
