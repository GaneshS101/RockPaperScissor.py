import random

options = ("Rock", "Paper", "Scissors")
running = True

while running:
    Player = None
    Computer = random.choice(options)
    
    while Player not in options:
        Player = input("Enter a choice (Rock, Paper, Scissors): ")

    print(f"Player: {Player}")
    print(f"Computer: {Computer}")

    if Player == Computer:
        print("It's a tie")
    elif Player == "Rock" and Computer == "Scissors":
        print("You Win!")
    elif Player == "Paper" and Computer == "Rock":
        print("You Win")
    elif Player == "Scissors" and Computer == "Paper":
        print("You Win!")
    else:
        print("You Lose!")

    if not input("Play Again? (y/n):").lower() == "y":
        running = False

print("Thank You For Playing!")