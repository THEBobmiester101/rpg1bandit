from player import Player
import random


DEFAULT_SHOP = {
    "A hearty meal":                        3,
    "Gamble":                               10,
    "Basic combat training":                15,
    "Services of a skilled weaponsmith":    40,
    "Services of a skilled tanner":         50,
    "Magic Shop: ring of the fleet fox":    65,
    "Magic Shop: vicious ring":             80,
    "Nothin' else":                         0
}
LINE_BREAK = "----------------------------------\n"
GAME_OPTIONS = "(FT) Find enemy to fight\n(RR) Rest and recover\n(SM) Spend money\n(ND) Next day\n(Q) Quit"
COMBAT_OPTIONS = ["Attack", "Dodge", "Run Away"]



class Game:
    
    player: Player
    n_days: int = 0


    def __init__(self, console_line_height):
        player_name = input("Choose a name for your character: ")
        self.player = Player(player_name, {})

        for line in range(console_line_height):
            print(self.player.catch_phrase if line == 4 else "\n")

    
    def __del__(self):
        print(self.player.name + "\'s journey ends.")
        print(f"Reached day {self.n_days}, killed {self.player.n_wins}, earned {self.player.n_gold} gold")


    def loop(self) -> bool:    
        is_daytime = True
        while is_daytime:
            player_input = input(LINE_BREAK + "What would you like to do?\n" + GAME_OPTIONS + "\n>")

            if player_input == "FT":
                enemy = self.getEnemyOptions()
                combat_result = self.fightSequence(enemy)
                if combat_result == "win":
                    self.player.n_wins += 1
                    print("You recovered " + str(enemy["gold"]) + " gold")
                    gold_total += enemy["gold"]
                    self.player.stats["gold"] += enemy["gold"]
                elif combat_result == "death":
                    if self.player.n_wins < 5:
                        print(self.player.name + " has died. They pressed their luck.")
                    elif self.player.n_wins < 10:
                        print(self.player.name + " was finally struck down.")
                    elif self.player.n_wins < 25:
                        print(self.player.name + "\'s luck caught up with them. It took a while.")
                    return False
                elif combat_result == "ran":
                    print("Made it out alive")

            elif player_input == "RR":
                pass

            elif player_input == "SM":
                print("What would you like to buy?")
                for key in DEFAULT_SHOP:
                    print(key + ": " + str(DEFAULT_SHOP[key]))
                item_index = int(input("(Enter 1-" + str(DEFAULT_SHOP.keys().__len__()) + ")")) - 1
                item_name = list(DEFAULT_SHOP.keys())[item_index]
                if item_name != "Nothin' else":
                    print(item_name)
                    if self.player.hasGold(DEFAULT_SHOP[item_name]):
                        self.player.stats["gold"] -= DEFAULT_SHOP[item_name]

            elif player_input == "ND":
                is_daytime = False
                print("Day " + str(self.n_days) + " ends")
                self.n_days += 1
                print("Day " + str(self.n_days) + " begins")

            elif player_input == "Q":
                return False

        return True


    def getEnemyOptions(self):
        enemy_stats = {
            "number": [], "attack": [], "crit": [], "natural_armor": [], "dodge": [], "health": [], "gold": []
        }

        for enemy in range(3):
            enemy_stats["number"].append(enemy + 1)
            enemy_stats["attack"].append(random.randint(1, 4))
            enemy_stats["crit"].append(random.randint(1, 3))
            enemy_stats["natural_armor"].append(random.randint(0, 2))
            enemy_stats["dodge"].append(random.randint(-2, 3))
            enemy_stats["health"].append(random.randint(1, 10) * 3)

        enemy_choice = int(self.reviewEnemies(enemy_stats)) - 1
        print("Chose enemy " + str(enemy_choice + 1))

        chosen_enemy = {
            "attack": enemy_stats["attack"][enemy_choice],
            "crit": enemy_stats["crit"][enemy_choice],
            "natural_armor": enemy_stats["natural_armor"][enemy_choice],
            "dodge": enemy_stats["dodge"][enemy_choice],
            "health": enemy_stats["health"][enemy_choice],
            "gold": enemy_stats["gold"][enemy_choice]
        }
        return chosen_enemy
    

    def fightSequence(self, enemy):
        fighting = True
        turn_count = 0

        # debugging; prints stats of player and enemy
        print("Player stats:\n" + str(self.player.stats.items()))
        print("\nEnemy stats:\n" + str(enemy.items()))

        while fighting:
            player_is_faster = (self.player.stats["dodge"] >= enemy["dodge"])
            if (turn_count == 0):
                if player_is_faster:
                    print("You make the first move")
                else:
                    print("They make the first move")

            # Player's turn. Whoever has higher dodge goes first.
            if (turn_count > 0) or player_is_faster:
                player_turn_choice = 2
                while player_turn_choice == 2:
                    player_turn_choice = int(input("What will you do? " + ", ".join(COMBAT_OPTIONS) + "?\n(1-" +
                                            str(COMBAT_OPTIONS.__len__()) + ")"))
                    if player_turn_choice == 1:
                        attack_damage = self.player.stats["attack"]
                        if random.randint(1, 4) == 4:
                            attack_damage += self.player.stats["crit"]
                        damage_dealt = max(0, attack_damage - enemy["natural_armor"] - enemy["dodge"])
                        enemy["health"] -= damage_dealt
                        if enemy["health"] <= 0:
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
            if (enemy["health"] > 0) and (fighting or (not player_is_faster)):
                attack_damage = enemy["attack"]
                if random.randint(1, 4) == 4:
                    attack_damage += enemy["crit"]
                damage_dealt = max(0, attack_damage - self.player.stats["natural_armor"] - self.player.stats["dodge"])
                self.player.stats["health"] -= damage_dealt
                if damage_dealt > 4:
                    print("\"I'm... about to pass out.\" You can't take another hit like that")
                elif damage_dealt > 1:
                    print("Took a nasty wound. That hurt like hell")
                elif damage_dealt == 1:
                    print("Took a minor wound")
                else:
                    print("They couldn't manage to wound you")

            turn_count += 1

            if enemy["health"] < 1:
                result = "win"
                fighting = False
            elif self.player.stats["health"] < 1:
                result = "death"
                fighting = False
            elif not fighting:
                result = "ran"
        return result
    

    def reviewEnemies(self, enemies: dict):
        for enemy in range(enemies["number"].__len__()):
            asessing_statements = []
            gold = 0
            """ An enemy's worth is determined by its other stats. Each tier is generally worth (tier^2 - 1)/2 gold. 
            Damage is not halved, because it makes the other stats much more effective.
            """

            damage = enemies["attack"][enemy] * 2 + enemies["crit"][enemy]
            if damage > 9:
                asessing_statements.append("very dangerous")
                gold += 15
            elif damage > 6:
                asessing_statements.append("dangerous")
                gold += 8
            elif damage > 3:
                asessing_statements.append("mildly dangerous")
                gold += 3
            else:
                asessing_statements.append("not very dangerous")
                # not worth gold

            toughness = enemies["natural_armor"][enemy] * 4 + enemies["health"][enemy]
            if toughness > 30:
                asessing_statements.append("very tough")
                gold += 7
            elif toughness > 20:
                asessing_statements.append("tough")
                gold += 4
            elif toughness > 10:
                asessing_statements.append("somewhat tough")
                gold += 1
            else:
                asessing_statements.append("not very tough")
                # not worth gold

            swiftness = enemies["dodge"][enemy]
            if swiftness > 2:
                asessing_statements.append("very agile")
                gold += 7
            elif swiftness > 0:
                asessing_statements.append("agile")
                gold += 4
            elif swiftness > -1:
                # asessing_statements.append("of normal speed")
                # not sure what a good way to say "average speed" is, probably best to not say anything
                gold += 1
            else:
                asessing_statements.append("unusually slow")
                # not worth gold

            enemies["gold"].append(gold)
            print("Enemy " + str(enemy + 1) + " is " + ", ".join(asessing_statements))
        choice = input("Which enemy would you like to face? Choose between " + str(enemies["number"]))
        return choice
    