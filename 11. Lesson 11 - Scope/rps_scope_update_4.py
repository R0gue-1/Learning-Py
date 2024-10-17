import sys
import random
from enum import Enum

game_count = 0 # to be removed in a future iteration of the game

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input('Enter ...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n')
   
    if playerchoice not in ["1","2","3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()
    
    player = int(playerchoice)

    pc_choice = random.choice('123')
    computer  = int(pc_choice)
    
    print('')
    print('You chose ' + str(RPS(player)).replace('RPS.', '') + '.')
    print('The computer chose ' + str(RPS(computer)).replace('RPS.', '') + '.')
    print('')
    
    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return 'You win 🎉🎉🎉🎉'
        elif player == 2 and computer == 1:
            return 'You win  🎉🎉🎉🎉'
        elif player == 3 and computer == 2:
            return 'You win  🎉🎉🎉🎉'
        elif player == computer:
            return 'Tie game 🪢'
        else:
            return '💻 The computer wins!'

    game_result = decide_winner(player, computer)
    print(game_result)

    # ACcessing global variable here
    global game_count 
    game_count += 1


    print("\nGame count: " + str(game_count))
    # this is cool if at the end player scores have not been implemented, I shall come back and add them

    print('\nPlay again?')
    while True:
        playagaain = input(' \nY for Yes or \nQ for Quit\n')
        if playagaain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagaain.lower() == "y":
        return play_rps()
    else:
        print('\n🎉🎉🎉🎉🎉🎉🎉')
        print('Thank you for playing! \n')
        sys.exit("Bye! 👋🏾")

play_rps()