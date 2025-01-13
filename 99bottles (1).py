#99 Bottles Lyrics

#Initialize

#Functions
def bottles():
    milk=100
    for i in range(100):
        if milk>1:
            for i in range(2):
                print(str(milk) + " bottles of milk on the wall")
            print("Take one down pass it around")
            milk=milk-1
            print(str(milk) + " bottles of milk on the wall")
            print(" ")
        else:
            for i in range(2):
                print(str(milk) + " bottle of milk on the wall")
            print("Take one down pass it around")
            print("No more bottles of milk on the wall")
            print("Boo Hoo!")

#Main
bottles()
