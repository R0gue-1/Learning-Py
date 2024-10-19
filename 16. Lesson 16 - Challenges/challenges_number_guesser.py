import random
import sys

def number_guesser(player_name='ReadyPlayer01'):
    # no longer need the player to specify their name somehow due to command line arguements
    # player_name = input("In this game the computer picks a number from 1 to 9 and you guess the number.\nEnter your name to begin: ")
   
    print(f"{player_name},\nWelcome to the NUMBER GUESSER GAME.\nIn this game the computer picks a number from 1 to 9 and you guess the number.\nYou score 1 point each time you guess right")

    pl_score = 0
    pc_score = 0
    no_tries = 0
    
    def play_game():
        nonlocal player_name
        nonlocal pl_score
        nonlocal pc_score
        nonlocal no_tries

        computer_guess = random.choice("1,2,3,4,5,6,7,8,9,0")
        player_guess = input(f"\nSelect a number from 0 - 9\nEnter your guess => ")

        if str(player_guess) not in ["1","2","3","4","5","6","7","8","9","0"]:
            print(f"\n{player_name}⚠️, you must enter a number")
            play_game()
        elif str(player_guess) == str(computer_guess):
            pl_score += 1
            no_tries += 1
            print(f"You win 🎉🎉🎉  {player_name}, lucky guess.\n")
        else:
            pc_score += 1
            no_tries += 1
            print(f"{player_name}!, You lost 🤣🤣🤣, unlucky guess I guess\n")
        

        print(f"{player_name} Score = {pl_score}\nComputer Score = {pc_score}\nNumber of Tries = {no_tries}\nYour win Percentage = {(pl_score/no_tries):.2%}\n\nDo you want to play again?")
        play_again = input("Enter Y for yes and N for NO\n\nYour Choice => ")

        if play_again.lower() == "y":
            play_game()
        elif str(player_guess).lower == "n":
            sys.exit("Bye! 👋🏾")
            
    return play_game

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

    play_guesser = number_guesser(args.name)
    play_guesser()

# GAME STARTS HAPENNING HERE no longer needed due to the addition of
# number_guesser()
