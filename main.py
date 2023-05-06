print("Game Hub")

print("Select one of the games you want to play in life")
print("1 - Coin flip")
print("2 - Rock Paper Scissor")
print("3 - Roll the dice")

user_choice = input("Enter a choice: ")


if user_choice == "1":
    import coin_flip

elif user_choice == "2":
    import rock_paper_scissors

else:
    import roll_the_dice