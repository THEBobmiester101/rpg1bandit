"""
Description here
"""
"""
IMPORTS GO HERE
"""
from game import Game
from shop import Shop



if __name__ == '__main__':
    game = Game(8)
    while game.loop():
        pass
    del game
