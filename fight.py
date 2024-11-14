from player import Player
from enemy import Enemy
from gameBase import *



COMBAT_OPTIONS = [
    "Attack", 
    "Dodge", 
    "Run Away"
]



class Fight:

    game: GameBase
    player: Player
    enemy: Enemy
    turn_count: int


    def __init__(self, game: GameBase, n_enemies: int):
        self.game = game
        self.player = game.player

        print()
        enemies = [Enemy() for _ in range(n_enemies)]
        for i, enemy in enumerate(enemies):
            print(f"Enemy {cstr(f'({i+1})', colors.GRAY)} is {enemy.assess()[0]}")
        print("Which enemy would you like to face?")
        i = GameBase.get_number_input(1, n_enemies)
        self.enemy = enemies[i - 1]
        
        self.turn_count = 0


    def __del__(self):
        # win
        if self.enemy.health == 0:
            self.player.n_wins += 1
            self.player.n_gold_earned += self.enemy.gold
            self.player.stats["gold"] += self.enemy.gold
            print(f"You recovered {cstr(self.enemy.gold, colors.YELLOW)} gold")
            self.game.end_day_script.append(f"Won a fight and got {self.enemy.gold} gold")

        # death
        elif self.player.health == 0:
            if self.player.n_wins < 5:
                print(f"{self.player.name} has died. They pressed their luck.")
            elif self.player.n_wins < 10:
                print(f"{self.player.name}\'s luck caught up with them. It took a while.")
            else:
                print(f"{self.player.name} was finally struck down. They left a legacy.")

        # flight
        else:
            print("Made it out alive")
            self.game.end_day_script.append(f"Ran away from a fight")


    def loop(self) -> bool:
        player_is_faster = self.player.dodge >= self.enemy.dodge
        
        if self.turn_count == 0:
            print(f"{'You' if player_is_faster else 'They'} make the first move")

        # enemy turn (skip first if player is faster)
        if not (self.turn_count == 0 and player_is_faster):
            if not self.__enemy_turn():
                return False

        print()

        # player turn
        if not self.__player_turn():
            return False

        self.turn_count += 1
        return True
    

    # returns true if fight should continue
    def __enemy_turn(self) -> bool:
        damage_dealt = self.enemy.strike(self.player)
        if damage_dealt > 4:
            self.player.say("I'm... about to pass out.")
            cprint("You can't take another hit like that", colors.RED)
        elif damage_dealt > 1:
            cprint("Took a nasty wound. That hurt like hell", colors.RED)
        elif damage_dealt == 1:
            cprint("Took a minor wound", colors.RED)
        else:
            cprint("They couldn't manage to wound you", colors.RED)

        return False if self.player.dead() else True


    # returns true if fight should continue
    def __player_turn(self) -> bool:
        while True:
            print("What will you do?")
            match GameBase.get_input_option(COMBAT_OPTIONS):
                case 1:
                    damage_dealt = self.player.strike(self.enemy)
                    print() # adds visual gap between combat turns
                    if self.enemy.dead():
                        cprint("A felling strike", colors.GREEN)
                        return False
                    elif damage_dealt > 4:
                        cprint("Strong attack", colors.GREEN)
                    elif damage_dealt > 1:
                        cprint("Dealt some damage", colors.GREEN)
                    elif damage_dealt == 1:
                        cprint("Barely hurt them...", colors.GREEN)
                    else:
                        cprint("Dealt no damage", colors.GREEN)
                    return True

                case 2:
                    print("This is no time for inaction, it's him or you!\n")

                case 3:
                    if self.player.dodge >= self.enemy.dodge:
                        self.player.say("Made it out of there...")
                    else:
                        print("They get off a parting shot")
                    return False