numbers = input("enter the numbers in the list")

if not numbers:
    print("The list is empty.")
else:
    max_num = numbers[0]
    min_num = numbers[0]

    for number in numbers:
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number

    print("Maximum number:", max_num)
    print("Minimum number:", min_num)
