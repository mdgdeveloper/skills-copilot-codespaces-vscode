# Write 'Hello world' to the console
# print('Hello world')

import random

OPTIONS = ["paper","rock","scissors"]
player_score = 0
computer_score = 0

# The game is in rounds and the player can select by the end of the round if he wants to continue or not
# The game ends when the player decides to stop playing
# The player can see the score at the end of each round
# The player can see the score at the end of the game

def main():
    print("Welcome to the game of Rock, Paper, Scissors")
    print("Please select an option")
    print("1. Play the game")
    print("2. Exit the game")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        play_game()
    elif choice == 2:
        print("Thank you for playing")
        exit()
    else:
        print("Invalid choice. Please select a valid option")
        main()

def updateScore(player, computer):
    global player_score
    global computer_score
    if player == computer:
        print("It's a tie")
    elif player == 1 and computer == 2:
        print("Computer wins")
        computer_score += 1
    elif player == 1 and computer == 3:
        print("Player wins")
        player_score += 1
    elif player == 2 and computer == 1:
        print("Player wins")
        player_score += 1
    elif player == 2 and computer == 3:
        print("Computer wins")
        computer_score += 1
    elif player == 3 and computer == 1:
        print("Computer wins")
        computer_score += 1
    elif player == 3 and computer == 2:
        print("Player wins")
        player_score += 1
    else:
        print("Invalid choice. Please select a valid option")
        play_game()

def play_game():
    print("Let's play the game")
    print("Please select an option")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    # Get information 
    player_choice = int(input("Enter your choice: "))
    computer_choice = random.randint(1,3)
    print("Player choice: ", OPTIONS[player_choice-1])
    print("Computer choice: ", OPTIONS[computer_choice-1])
    # Update the score
    updateScore(player_choice, computer_choice)
    
    # Ask the player if he wants to continue playing
    print("Do you want to continue playing?")
    print("1. Yes")
    print("2. No")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        play_game()
    elif choice == 2:
        print("Thank you for playing")
        # Show the score
        print("Player score: ", player_score)
        print("Computer score: ", computer_score)
        exit()
    else:
        print("Invalid choice. Please select a valid option")
        play_game()

main()