from gameBase import GameBase
from player import Player
from enemy import Enemy
from shop import Shop
from fight import Fight
import random



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
        self.player = Player(player_name, {})
        self.shop = Shop()

        for _ in range(console_line_height):
            print()
        self.newDay()

    
    def __del__(self):
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
                self.newDay()

            case 5:
                return False
        
        print()
        return True


    def newDay(self):
        if self.n_days > 0:
            self.day_events_list.append(f"^^ Day {self.n_days} summary ^^")
            self.player.playerHeal()
            self.can_fight, self.can_rest = True, True

            # prints all statements that were added to self.end_day_script throughout the day
            print(LINE_BREAK)
            print('\n'.join(self.day_events_list))
        self.n_days += 1
        print(LINE_BREAK)
        print(f"Day {self.n_days} begins")

        self.day_events_list.clear()
        if self.n_days > 1:
            self.player.assess_health()
        else:
            self.player.say(self.player.catch_phrase)

        print(LINE_BREAK)
