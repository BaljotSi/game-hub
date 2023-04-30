# Roll the dice game

import random

random_number = random.randint(1,6)



for i in range(3):
    users_choice = int(input("Enter the number you are guessing!(1 to 6)"))
    if users_choice == random_number:
        print("you got the correct number! CONGRATULATIONS!")
        break

    else:
        print("wrong answer")
        print("You have " , 3-i , "attempt/s left")
