import time

from game import Game

game_instance = Game()
game_instance.make_matrix()

if __name__ == "__main__":
    while True:
        game_instance.calculate_steps()
        time.sleep(1) # Add a one second pause to reduce flashing.
        game_instance.display()
