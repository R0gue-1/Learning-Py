import sys
from rps_cargs_update_8 import rps
from challenges_number_guesser import number_guesser

def play_game(name='ReadyPlayer1'):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playerchoice = input("\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\n or press \"x\" to exit the ARcade\n\n")

        if playerchoice not in ["1","2","x"]:
            print(f"\n{name}, please enter 1, 2, 3, or x")
            return play_game(name)
        
        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = number_guesser(name)
            guess_my_number()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Provides a personalized game experience.")

    parser.add_argument('-n','--name', metavar='name',required=True,help="The name of the person playing the game.")

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🕹️🕹️🕹️")

    play_game(args.name)