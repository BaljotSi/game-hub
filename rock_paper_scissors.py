import random 

game = ("rock" , "paper" , "scissors")

computer = random.choice(game)


user = input("Enter your choice ( r , p , s ) ")

if computer == user:
    print("draw")
elif computer == "rock":
    if user == "s":
        print("You lost badly")
    else:
        print("I guess you win")
elif computer == "scissors":
    if user == "p":
        print("You lost badly")
    else:
        print("I guess you win")
elif computer == "paper":
    if user == "r":
        print("You lost badly")
    else:
        print("I guess you win")

    