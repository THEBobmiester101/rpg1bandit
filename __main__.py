from game import Game


if __name__ == '__main__':
    game = Game(8)
    while game.loop():
        pass
    del game
