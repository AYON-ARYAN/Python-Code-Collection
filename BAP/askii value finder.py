a = input("Enter a digit or anything you want to get the ASCII values for: ")

for char in a:
    if char.isalpha():
        ascii_value = ord(char)
        print(f"The ASCII value of '{char}' is {ascii_value}")
    elif char.isdigit():
        digit_value = int(char)
        print(f"The ASCII value of the digit '{char}' is {digit_value}")
    else:
        print(f"Cannot determine ASCII value for '{char}'. Skipped.")

