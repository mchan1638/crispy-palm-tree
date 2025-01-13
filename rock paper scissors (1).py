#Rock Paper Scissors

#Initialize
import random

#Functions
def game():
    while True: #Infinite Loop
        print("Welcome to Rock Paper Scissors!")
        player = input("What do you choose? (Rock/Paper/Scissors)").lower()
        ans = random.randint(1,3)
        if ans == 1:
            ans = "Rock"
        if ans == 2:
            ans = "Paper"
        if ans == 3:
            ans = "Scissors"
        print("Player (you): " + player.capitalize())
        print("Computer: " + ans)
        if player == "rock" and ans == "Scissors" or player == "paper" and ans == "Rock" or player == "scissors" and ans == "Paper":
            print("You Won!")
        elif player.capitalize() == ans:
            print("Draw!")
        elif player == "rock" and ans == "Paper" or player == "paper" and ans == "Scissors" or player == "scissors" and ans == "Rock":
            print("You Lost!")
        print(" ")
        play = input("Play Again? (Yes/No)").lower()
        if play == "no":
            print("Thank you for playing!")
            break #Breaks loop

#Main
game()
