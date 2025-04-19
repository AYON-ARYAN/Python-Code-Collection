def number(s):
    upper = 0
    lower = 0  
    
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
            
    return upper, lower


s = str(input("Enter the string you want to check it for: "))
upper, lower = number(s)

print("UPPER CASE:", upper)
print("LOWER CASE:", lower)

