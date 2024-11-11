from gameBase import GameBase
from player import Player
from enemy import Enemy
from shop import Shop
import random



LINE_BREAK = "----------------------------------"
GAME_OPTIONS = [
    "Find enemy to fight",
    "Rest and recover",
    "Visit shop",
    "Next day",
    "Quit"
]
COMBAT_OPTIONS = [
    "Attack", 
    "Dodge", 
    "Run Away"
]



class Game(GameBase):
    
    player: Player
    shop: Shop
    n_days: int = 1
    can_fight: bool = True
    can_rest: bool = True
    bought_items = []


    def __init__(self, console_line_height):
        player_name = input("Choose a name for your character: ")
        self.player = Player(player_name, {})
        self.shop = Shop()

        for _ in range(console_line_height):
            print()
        self.end_day_script.append(f"{self.player.catch_phrase}\nDay 1 begins")

    
    def __del__(self):
        print(self.player.name + "\'s journey ends.")
        print(f"Reached day {self.n_days}, killed {self.player.n_wins}, earned {self.player.n_gold_earned} gold")


    def loop(self) -> bool:    
        self.newDay()

        while True:
            print("What would you like to do?")
            match GameBase.get_input_option(GAME_OPTIONS):
                case 1:
                    if not self.can_fight:
                        print("You're taking it easy today, remember?")
                        break   # skip following instructions if you can't fight
                    
                    self.can_rest = False
                    enemy = self.getEnemyOptions()
                    match self.fightSequence(enemy):
                        case "win":
                            _, enemy_gold = enemy.assess()
                            self.player.n_wins += 1
                            print(f"You recovered {enemy_gold} gold")
                            self.player.n_gold_earned += enemy_gold
                            self.player.stats["gold"] += enemy_gold
                            self.end_day_script.append(f"Won a fight and got {enemy_gold} gold")
                        case "death":
                            if self.player.n_wins < 5:
                                print(self.player.name + " has died. They pressed their luck.")
                            elif self.player.n_wins < 10:
                                print(self.player.name + "\'s luck caught up with them. It took a while.")
                            elif self.player.n_wins < 25:
                                print(self.player.name + " was finally struck down. They left a legacy.")
                            return False
                        case "ran":
                            self.end_day_script.append("Ran away from a fight")
                            print("Made it out alive")
                    
                case 2:
                    if self.can_rest:
                        self.player.playerHeal()
                        self.can_fight, self.can_rest = False, False
                        self.end_day_script.append("Rested for most of the day")
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
                    self.end_day_script.append(f"Day {self.n_days} ends")
                    break

                case 5:
                    return False
            
            print()

        return True


    def newDay(self):
        self.n_days += 1

        self.player.playerHeal()
        self.can_fight, self.can_rest = True, True

        # prints all statements that were added to self.end_day_script throughout the day
        end_day_str = '\n'.join(self.end_day_script)
        print(f"{LINE_BREAK}\n{end_day_str}\n{LINE_BREAK}")
        self.end_day_script.clear()
        self.end_day_script.append(f"Day {self.n_days} begins")


    def getEnemyOptions(self):
        enemies = [Enemy() for _ in range(3)]
        print()
        enemy_choice = self.reviewEnemies(enemies)
        print(f"Chose enemy {enemy_choice}")
        return enemies[enemy_choice - 1]
    

    def reviewEnemies(self, enemies: list[Enemy]):
        for i, enemy in enumerate(enemies):
            print(f"Enemy {i+1} is {enemy.assess()[0]}")

        print("Which enemy would you like to face?")
        choice = GameBase.get_number_input(1, enemies.__len__())
        return choice
    

    def fightSequence(self, enemy: Enemy):
        fighting = True
        turn_count = 0

        # debugging; prints stats of player and enemy
        #print("Player stats:\n" + str(self.player.stats.items()))
        #print("\nEnemy stats:\n" + str(enemy.items()))

        while fighting:
            player_is_faster = (self.player.dodge >= enemy.dodge)
            if (turn_count == 0):
                if player_is_faster:
                    print("You make the first move")
                else:
                    print("They make the first move")

            # Player's turn. Whoever has higher dodge goes first.
            if (turn_count > 0) or player_is_faster:
                player_turn_choice = 2
                while player_turn_choice == 2:
                    print("What will you do?")
                    player_turn_choice = GameBase.get_input_option(COMBAT_OPTIONS)
                    if player_turn_choice == 1:
                        damage_dealt = self.player.strike(enemy)
                        print() # adds visual gap between combat turns
                        if enemy.dead():
                            print("A felling strike")
                        elif damage_dealt > 4:
                            print("Strong attack")
                        elif damage_dealt > 1:
                            print("Dealt some damage")
                        elif damage_dealt == 1:
                            print("Barely hurt them...")
                        else:
                            print("Dealt no damage")

                    elif player_turn_choice == 2:
                        print("This is not time for inaction, it's him or you!")

                    elif player_turn_choice == 3:
                        if player_is_faster:
                            print("\"Made it out of there...\"")
                        else:
                            print("They get off a parting shot")
                        fighting = False

            # Enemy's turn. Whoever has higher dodge goes first.
            if (not enemy.dead()) and (fighting or (not player_is_faster)):
                damage_dealt = enemy.strike(self.player)
                if damage_dealt > 4:
                    print("\"I'm... about to pass out.\" You can't take another hit like that")
                elif damage_dealt > 1:
                    print("Took a nasty wound. That hurt like hell")
                elif damage_dealt == 1:
                    print("Took a minor wound")
                else:
                    print("They couldn't manage to wound you")
                if self.player.dead():
                    return "death"

            turn_count += 1

            if enemy.dead():
                result = "win"
                fighting = False
            elif not fighting:
                result = "ran"

        return result
