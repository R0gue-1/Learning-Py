import sys
import random
from enum import Enum

def rps():
    game_count = 0 
    player_wins = 0
    computer_wins = 0
    game_ties = 0

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins
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
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal game_ties


            if player == 1 and computer == 3:
                player_wins += 1
                return 'You win 🎉🎉🎉🎉'
            elif player == 2 and computer == 1:
                player_wins += 1
                return 'You win  🎉🎉🎉🎉'
            elif player == 3 and computer == 2:
                player_wins += 1
                return 'You win  🎉🎉🎉🎉'
            elif player == computer:
                game_ties += 1
                return 'Tie game 🪢'
            else:
                computer_wins += 1
                return '💻 The computer wins!'

        game_result = decide_winner(player, computer)
        print(game_result)

        # ACcessing global variable here
        nonlocal game_count 
        game_count += 1


        print("\nGame count: " + str(game_count))
        print("\nPlayer Score: " + str(player_wins))
        print("Computer Score: " + str(computer_wins))
        print("Ties: " + str(game_ties))
        
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
        
    return play_rps #rerurning th efunction not calling it into action

# play_rps() # cant call rps now since it is no longer a global function

play = rps()
play()