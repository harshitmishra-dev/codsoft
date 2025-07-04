import random

user_score=0
comp_score=0

def get_winner(user,comp):
    if user==comp:
        return "Tie"
    elif (user=="rock" and comp=="scissors") or \
         (user=="scissors" and comp=="paper") or \
         (user=="paper" and comp=="rock"):
        return "User"
    else:
        return "Computer"

print("Welcome to Rock-Paper-Scissors Game!")
print("Instructions:")
print("Type rock, paper or scissors to play.")
print("Type exit to quit the game.\n")

while True:
    user=input("Enter your choice: ").lower()
    if user=="exit":
        print("Final Scores -> You:",user_score,"Computer:",comp_score)
        print("Thanks for playing!")
        break
    if user not in ["rock","paper","scissors"]:
        print("Invalid input. Please type rock, paper or scissors.\n")
        continue

    comp=random.choice(["rock","paper","scissors"])
    print("Computer chose:",comp)
    winner=get_winner(user,comp)

    if winner=="User":
        print("You win this round!\n")
        user_score+=1
    elif winner=="Computer":
        print("Computer wins this round!\n")
        comp_score+=1
    else:
        print("It's a tie!\n")

    print("Current Score -> You:",user_score,"Computer:",comp_score)
    print("-"*40)
