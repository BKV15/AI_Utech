from hanged import Hanged_Man
from info import *

def main_game():

    game_start()

    while True:

        game = Hanged_Man()
        game.difficulty_level()
        game.pick_word()
        game.word_encryption()
        game.turns()
        game.display()
        game_is_finished = False

        while not(game_is_finished):

            game.update_secret_world()
            game.display()
            game_is_finished = game.game_state()
        
        if game.num_turns == 0:
            print(f'The correct word was : {game.random_word}')
            game_lose()
        else:
            game_win()
        
        play_again = input('Do You want to play another game ? Y/N').lower()

        if play_again == 'y':
            print('\n' * 100)
            continue
        else:
            print('Thanks for playing')
            break

main_game()

