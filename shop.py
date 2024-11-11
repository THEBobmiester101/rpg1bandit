from gameBase import GameBase
from player import Player
from article import ImmediateArticle, Item, gamble



class Shop:

    articles: dict = {}

    
    def __init__(self):
        self.articles = {
            ImmediateArticle("A hearty meal",                     3 ): 100,
            ImmediateArticle("Gamble",                            10, gamble): -1,
            ImmediateArticle("Basic combat training",             15): 2,
            ImmediateArticle("Services of a skilled weaponsmith", 40): 2,
            ImmediateArticle("Services of a skilled tanner",      50): 2,
            Item(            "Magic Shop: ring of the fleet fox", 65): 1,
            Item(            "Magic Shop: vicious ring",          80): 1,
            ImmediateArticle("Nothin' else",                      0 ): -.1
        }


    def loop(self, game: GameBase, player: Player) -> bool:
        self.articles = dict(sorted(
            self.articles.items(), key = lambda x: abs(x[1]), reverse = True))

        print(f"What would you like to buy? (You have {player.stats['gold']} gold)\n")

        i = 1
        for article, quantity in self.articles.items():
            if quantity > 0:
                print(f"({i}) {article.name: <40} {article.cost: >10} gold {quantity: >10} pcs")
            elif quantity < 0:
                print(f"({i}) {article.name: <40} {article.cost: >10} gold")
            i += 1

        i = GameBase.get_number_input(1, self.articles.items().__len__()) - 1
        article = list(self.articles.keys())[i]

        if article.name == "Nothin' else":
            return False
        
        if player.has_gold(article.cost):
            player.stats["gold"] -= article.cost
            if self.articles[article] > 0:
                self.articles[article] -= 1
            if article is Item:
                player.items.append(article)
            print(f"Purchased: {article.name}")
            article.immediate(player, article.cost)
            game.end_day_script.append(f"Bought: {article.name}")
            
        else:
            print(f"Sorry pal, you ain't got the cash")

        return True
    