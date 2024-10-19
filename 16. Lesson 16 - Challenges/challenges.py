# 1. GUESSING NUMBER GAME

import random

def guess_number():
    player_score = 0
    computer_score = 0
    game_count = 0

    def play_guess():
        nonlocal player_score
        nonlocal computer_score
        nonlocal game_count

        player_name = input("Tell the computer your name: ")
        computer_guess = random.choice("123")
        player_number = input(f"Welcome {player_name}, Get ready to start\n{player_name}, guess which number the computer is thinking of: ")
        
        if player_number == computer_guess:
            player_score += 1
            print(f"{player_name} Wins")
        else:
            computer_score += 1
            print("computer wins")

        replay = input("Replay?\nY=yes\nN=No\nYour response: ")
        if replay.lower() == "y":
            continue
        
    return play_guess
    

        
guess_number()