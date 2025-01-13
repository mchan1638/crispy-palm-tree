#Multiplication Quiz

#Initialize
import random
import time

#Functions
def multiplication_quiz():
    print("Welcome to the Multiplication Quiz! What difficulty would you like?")
    difficulty = input("What difficulty would you like? (Easy/Medium/Hard)").lower() #player selects difficulty
    if difficulty == "easy": #the easier the difficulty, the smaller the numbers multiplied will be
        numrange = 9
    elif difficulty == "medium":
        numrange = 15
    elif difficulty == "hard": #the harder the difficulty, the bigger the numbers multiplied will be
        numrange = 100
    questionnum = 0 #shows what question the user is on/how many questions they've answered
    score = 0 #gives the user their final score at the end/counts correct and incorrect
    print("How many questions would you like to answer?")
    questions = int(input("How many questions would you like to answer?")) #player selects number of questions they want to answer
    start_time = time.time() #starts timer
    for i in range(questions): #repeats for the amount of questions player wanted to answer
        questionnum=questionnum+1
        print(" ")
        print("Question " + str(questionnum))
        num1 = random.randint(0,numrange)
        num2 = random.randint(0,numrange)
        print("What is " + str(num1) + " x " + str(num2) + "?") #asks math question
        ans = int(input("What is " + str(num1) + " x " + str(num2) + "?")) #answer math question
        print("Your Answer: " + str(ans))
        if ans == num1*num2: #checks if the answer is correct
            print("Correct!")
            score = score + 1 #increases the score if it's correct
        else:
            print("Incorrect")
    end_time = time.time() #ends timer
    elapsed_time = end_time - start_time
    print("Your Score: " + str(score) + "/" + str(questions)) #gives final score
    print("You completed your quiz in " + str(elapsed_time) + " seconds!") #gives time completed in

#Main
multiplication_quiz()
