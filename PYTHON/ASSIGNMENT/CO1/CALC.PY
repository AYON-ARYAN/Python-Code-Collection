while True:
    y = int(input("Do you want to continue? (1 for Yes, 0 for No): "))
    if y == 0:
        break
    elif y == 1:
        i = int(input("Do you want to do calculations? (1 for Yes, 0 for No): "))
        if i == 1:
            a = int(input("What operation do you want to do?\nPress 1 for: +\nPress 2 for: *\nPress 3 for: /\nPress 4 for: -\nEnter operation number: "))
            if a == 1:
                print("\nAddition")
                b = int(input("Enter the first number to add: "))
                c = int(input("Enter the second number to add: "))
                print(f"The answer is {b} + {c} = {b + c}")
            elif a == 2:
                print("\nMultiplication")
                b = int(input("Enter the first number to multiply: "))
                c = int(input("Enter the second number to multiply: "))
                print(f"The answer is {b} * {c} = {b * c}")
            elif a == 3:
                print("\nDivision")
                b = int(input("Enter the first number to divide: "))
                c = int(input("Enter the second number to divide: "))
                if c != 0:
                    print(f"The answer is {b} / {c} = {b / c}")
                else:
                    print("Error: Division by zero!")
            elif a == 4:
                print("\nSubtraction")
                b = int(input("Enter the first number to subtract: "))
                c = int(input("Enter the second number to subtract: "))
                print(f"The answer is {b} - {c} = {b - c}")
        elif i == 0:
            print("No calculations performed.")
        else:
            print("Invalid input for calculations flag.")
    else:
        print("Invalid input for continue flag.")
