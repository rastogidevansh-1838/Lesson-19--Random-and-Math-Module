import random
while True:
    user_action = input("Enter a choice (rock, paper or scissors): ")
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\n You chose {user_action}, computer chose{computer_action}")
    if user_action == computer_action:
        print(f"both players selected {user_action}. It's a tie!!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rocks smashes Scissors, You win!")
        else:
            print("Paper covers Rock, You lose!")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock, You win!")
        else:
            print("Scissors cut Paper, You lose!")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissor cuts Paper, You win!")
        else:
            print("Rock smashes Scissor, You lose!")
    play_again = input("Play Again? (Y/N): ")
    if play_again !="Y":
        break