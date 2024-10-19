import sys
import random
from enum import Enum

def rps(name='ReadyPlayer01'):
    game_count = 0 
    player_wins = 0
    computer_wins = 0
    game_ties = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(f"{name}, please enter ...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n")
    
        if playerchoice not in ["1","2","3"]:
            print(f"{name}, please you must enter 1, 2, or 3.")
            return play_rps()
        
        player = int(playerchoice)

        pc_choice = random.choice('123')
        computer  = int(pc_choice)
        
        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()}")
        print(f"The computer chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal game_ties

            if player == 1 and computer == 3:
                player_wins += 1
                return f'{name}, you win 🎉🎉🎉🎉'
            elif player == 2 and computer == 1:
                player_wins += 1
                return f'{name}, you  🎉🎉🎉🎉'
            elif player == 3 and computer == 2:
                player_wins += 1
                return f'{name}, you  🎉🎉🎉🎉'
            elif player == computer:
                game_ties += 1
                return 'Tie game 🪢'
            else:
                computer_wins += 1
                return f'💻 The computer wins!\nSorry,{name}...🥲'

        game_result = decide_winner(player, computer)
        print(game_result)

        # ACcessing global variable here
        nonlocal game_count 
        game_count += 1


        print(f"\nGame count: {str(game_count)}")
        print(f"\n{name}'s Score: {str(player_wins)}")
        print(f"Computer Score: {str(computer_wins)}")
        print(f"Ties: {str(game_ties)}")
        
        print(f'\nPlay again, {name}?')
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
            print(f'Thank you, {name} for playing! \n')
            sys.exit(f"Bye {name}! 👋🏾")
        
    return play_rps #rerurning th efunction not calling it into action


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personalised game experience." 
    )

    parser.add_argument(
        "-n", "--name", metavar="name", #dest="firstname"
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()