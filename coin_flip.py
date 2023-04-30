import random

coin = ("head" , "tail")
toss = random.choice(coin)

option = input("Enter heads or tails ")

if option == toss:
    print("Congratulations! You Won!")
else:
    print("It Wasn't" ,option)
