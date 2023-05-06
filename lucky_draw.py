from random import randint

lucky_draw = randint(1,1000)

user = int(input("pick a number from 1 to 1000 "))

if lucky_draw == user:
    print("You won")
else:
    print("You didn't win")
    print("the lucky draw was", lucky_draw)