#Name Generator Activity

#Functions
def game():
    print("Welcome!")
    print("Answer the questions to see which Winx Club fairy you are")
    ans = input("What weather do you prefer? (Hot/Cold)").lower() #first branch
    if ans == "hot":
        ans = input("Which activity do you prefer? (Reading/Sports)").lower() #second branch
        if ans == "reading":
            ans = input("Which fairytale creature do you prefer? (Dragons/Nymphs)").lower() #third branch
            if ans == "dragons":
                print("You are Bloom!") #fourth branch
            else:
                print("You are Daphne!") #fourth branch
        else:
            ans = input("What do you like to do at the beach? (Playing with Sand/Swimming)").lower() #third branch
            if ans == "playing with sand":
                print("You are Stella!") #fourth branch
            else:
                print("You are Aisha!") #fourth branch
    else:
        ans = input("Do you prefer being outside or inside? (Outside/Inside)").lower() #second branch
        if ans == "outside":
            ans = input("Do you prefer plants or animals? (Plants/Animals)").lower() #third branch
            if ans == "plants":
                print("You are Flora!") #fourth branch
            else:
                print("You are Roxy!") #fourth branch
        else:
            ans = input("Which hobby do you prefer? (Music/Coding)").lower() #third branch
            if ans == "music":
                print("You are Musa!") #fourth branch
            else:
                print("You are Tecna!") #fourth branch
    print(" ")
    print("Play Again?")
    ans = input("Play Again?").lower()
    if ans == "yes":
        game()
    else:
        print("Thank you for playing!")

#Main
game()
