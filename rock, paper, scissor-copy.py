import random
import os

os.system("cls")
options = ["rock", "paper", "scissors"]
print("Are you ready to play Rock, Paper, Scissors?")
users_points = 0
comps_points = 0
user_pick = ["rock", "paper", "scissors", "q"]

while True:
    ans = input("\nType 'yes' if you want to play or 'no' if not: ").lower()

    if ans == "yes":
        rounds = int(input("Enter the number of rounds you want to play: "))
        for round_num in range(1, rounds + 1):
            print(f"\nRound {round_num}:")

            user = input("Choose between rock, paper, scissors, or 'q' to quit: ").lower()

            if user == "q":
                break
            if user not in user_pick:
                print("\nInvalid Option, Try again.")
                continue

            pick = random.randint(0, 2)
            computer = options[pick]
            print("Computer chose ", computer)

            if user == computer:
                print("It's a tie")
            elif (user == "rock" and computer == "scissors") or \
                    (user == "paper" and computer == "rock") or \
                    (user == "scissors" and computer == "paper"):
                print("You won! 👏👏👏 and computer lost")
                users_points += 1
            else:
                print("\nYou lost and computer won. Try again.")
                comps_points += 1

            # Display scores after each round
            print(f"\nScores after Round {round_num} - You: {users_points}, Computer: {comps_points}")

        # Check and print the winner after all rounds
        if users_points > comps_points:
            print("\nYou won the game!!!\nFinal Scores - You: {}, Computer: {}".format(users_points, comps_points))
        elif comps_points > users_points:
            print("\nComputer won the game!!!\nFinal Scores - You: {}, Computer: {}".format(users_points, comps_points))
        else:
            print("\nIt's a tie!\nFinal Scores - You: {}, Computer: {}".format(users_points, comps_points))
    elif ans == "no":
        os.system('cls')
        print("Goodbye")
        break
    else:
        print("\nInvalid Option, Try again.")

os.system('cls')
print("Goodbye")
