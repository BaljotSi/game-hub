from random import randint

computer = randint(1,6)

user = input("Odd or Even, YOU make the choice. ")

if computer % 2 == 0: # even
    if user == "e":
        print("Your are safe and win")
    else:
        print("We are going to shoot you.")

else:
    if user == "o":
        print("Your are safe and win")
    else:
        print("We are going to shoot you.")

 

