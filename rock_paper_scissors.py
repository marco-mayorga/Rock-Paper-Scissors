import random

options = ["Rock", "Paper" , "Scissors"]

def play_again():
    play_Again = input(f"Play again? [y/n]: ").lower()
    if play_Again == "y":
        gameloop()
    elif play_Again == "n":
        print("Thanks For playing")
    else:
        print("Not a valid answer")
        play_again()

def gameloop():
    while True:
        player_Choice = input(f"Choose Rock, Paper, or Scissors: ").capitalize()
        cpu_Choice = random.choice(options)
        if player_Choice == cpu_Choice:
            print(f"Computer: {cpu_Choice}")
            print(f"Player: {player_Choice}")
            print("You Both Tied!")
        elif player_Choice == options[0]:
            if cpu_Choice == options[1]:
                print(f"Computer: {cpu_Choice}")
                print(f"Player: {player_Choice}")
                print("Computer Wins!")
            elif cpu_Choice == options[2]:
                print(f"Computer: {cpu_Choice}")
                print(f"Player: {player_Choice}")
                print("Player Wins!")
        elif player_Choice == options[1]:
            if cpu_Choice == options[2]:
                print(f"Computer: {cpu_Choice}")
                print(f"Player: {player_Choice}")
                print("Computer Wins!")
            elif cpu_Choice == options[0]:
                print(f"Computer: {cpu_Choice}")
                print(f"Player: {player_Choice}")
                print("Player Wins!")
        elif player_Choice == options[2]:
            if cpu_Choice == options[0]:
                print(f"Computer: {cpu_Choice}")
                print(f"Player: {player_Choice}")
                print("Computer Wins!")
            elif cpu_Choice == options[1]:
                print(f"Computer: {cpu_Choice}")
                print(f"Player: {player_Choice}")
                print("Player Wins!")
        play_again()
        break

gameloop()