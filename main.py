print("Game Hub")

while True:
    print()
    print("*"*25)
    print()
    print("Select one of the games you want to play in life")
    print("1 - Coin flip")
    print("2 - Rock Paper Scissor")
    print("3 - Lucky Draw")
    print("4 - Roll the dice")
    print("5 - Marbles")
    print("Q - To Exit the game")

    user_choice = input("Enter a choice: ")


    if user_choice == "1":
        import coin_flip

    elif user_choice == "2":
        import rock_paper_scissors

    elif user_choice == "3":
        import lucky_draw

    elif user_choice == "4":
        import roll_the_dice

    elif user_choice == "Q":
        print("Thanks for playing the game")
        break

    else:
        print("Input Invalid!")