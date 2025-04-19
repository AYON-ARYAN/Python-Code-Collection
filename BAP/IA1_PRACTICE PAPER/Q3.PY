
s = input("Enter a sentence: ")


letter = 0
digit = 0


for char in s:
    if char.isalpha(): 
        letter += 1
    elif char.isdigit(): 
        digit += 1


print("LETTERS", letter)
print("DIGITS", digit)
