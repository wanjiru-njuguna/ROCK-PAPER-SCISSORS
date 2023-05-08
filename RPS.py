import random


available_choices = ["rock", "paper", "scissors"]

users_score = 0

computer_score = 0

random_number = random.randint(0,2) 

computers_choice = available_choices[random_number]

while True:

    user_choice = input("please enter rock, paper or scissors to play or q to quit the game. ").lower()


    print(f" The computer's choice was, {computers_choice}")

    if user_choice == "q":
        break
    elif user_choice not in available_choices:
        continue
    elif user_choice == "rock" and computers_choice == "scissors":
        print("You won!")
        users_score += 1

    elif user_choice == "paper" and computers_choice == "rock":
        print("You won!")
        users_score += 1

    elif user_choice == "scissors" and computers_choice == "paper":
            print("You won!")
            users_score += 1
    else:
            print("You lost!")
            computer_score += 1

print(f" Your total score is {users_score} and the computer score is {computer_score}")
print("Goodbye! Thanks for playing!")

       
