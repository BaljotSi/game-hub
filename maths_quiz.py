from random import randint

while True:

    first = randint(0,100)
    second = randint(0,10)

    answer = first + second

    user = int(input(f"{first}+{second} "))

    if user == answer:
       print("oi Ya got it correct fella")
    elif user == "x":
        break
    else:
        print("your a dumb fella, ain't ya")