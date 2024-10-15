import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagaain = True

while playagaain:
    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

    # value = input('message to the user:\n')

    # print(value)

    print('')
    playerchoice = input('Enter ...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n')
    cast_playerchoice = int(playerchoice)

    if cast_playerchoice < 1 or cast_playerchoice > 3:
        sys.exit('You must enter 1,2, or 3')

    pc_choice = random.choice('123')
    cast_pc_choice  = int(pc_choice)

    print('')
    print('You chose ' + str(RPS(cast_playerchoice)).replace('RPS.', '') + '.')
    print('The computer chose ' + str(RPS(cast_pc_choice)).replace('RPS.', '') + '.')
    print('')

    if cast_playerchoice == 1 and cast_pc_choice == 3:
        print('You win 🎉🎉🎉🎉')
    elif cast_playerchoice == 2 and cast_pc_choice == 1:
        print('You win  🎉🎉🎉🎉')
    elif cast_playerchoice == 3 and cast_pc_choice == 2:
        print('You win  🎉🎉🎉🎉')
    elif cast_playerchoice == cast_pc_choice:
        print('Tie game 🪢')
    else:
        print('💻 The computer wins!')

    print('')

    playagaain = input('\nPlay again \nY for Yes or \nQ for Quit\n\n')

    if playagaain.lower() == "y":
        continue
    else:
        print('\n🎉🎉🎉🎉🎉🎉🎉')
        print('Thank you for playing! \n')
        playagaain = False
        # break 
sys.exit("Bye! 👋🏾")