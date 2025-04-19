a = input("Enter 1 to convert Fahrenheit to Celsius or 2 to convert Celsius to Fahrenheit: ")

if a == '1':
    fa = float(input("Enter temperature in Fahrenheit: "))
    cel = (fa - 32) * 5/9
    print(f"{fa} Fahrenheit is equal to {cel:.2f} Celsius")

elif a == '2':
    cel = float(input("Enter temperature in Celsius: "))
    fa = (cel * 9/5) + 32
    print(f"{cel} Celsius is equal to {fa:.2f} Fahrenheit")

else:
    print("Invalid input. Please enter 1 or 2.")
