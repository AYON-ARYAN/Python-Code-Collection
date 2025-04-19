o = float('-inf')


for i in range(5):
    n = int(input(f"Enter integer {i + 1}: "))  
    if n > o:
        o = n

print(f"The greatest number is: {o}")
