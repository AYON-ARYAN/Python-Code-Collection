import random

# Instructions of the game
print("<--------------------------------------------------------Rock🪨 Paper📃 Scissors✂---------------------------------------------------------")
print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

while True:
    print("Enter choice \n 1 for Rock🪨 \n 2 for paper📃 \n 3 for scissor✂ \n")

    # take the input from user
    choice = int(input("User turn: "))
    result = ""


    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        choice_name = 'Rock🪨'
    elif choice == 2:
        choice_name = 'Paper📃'
    else:
        choice_name = 'Scissor✂️'

    # print user choice
    print("user choice is: ",choice_name)
    print("\nNow its computer turn.......")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock🪨'
    elif comp_choice == 2:
        comp_choice_name = 'Paper📃'
    else:
        comp_choice_name = 'Scissor✂'

    print("Computer choice is: ", comp_choice_name)

    print(choice_name + " V/s ", comp_choice_name)
    # For Draw
    if choice == comp_choice:
        print("Draw=> ", end="")
        result += "Draw"

        # For Winning
        if ((choice == 1 and comp_choice == 2) or
                (choice == 2 and comp_choice == 1)):
            print("paper wins => ", end="")
            result = "Paper📃"

        elif ((choice == 1 and comp_choice == 3) or
              (choice == 3 and comp_choice == 1)):
            print("Rock wins =>", end="")
            result = "Rock🪨"
        else:
            print("scissor wins =>", end="")
            result = "Scissor✂"

    # Printing either user or computer wins or draw
    if result == "Draw":
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    ans = input("Do you want to play again? (Y/N)")

    if ans in 'nN':
        break

# Thanking the user for playing
print("\nThanks for playing")
