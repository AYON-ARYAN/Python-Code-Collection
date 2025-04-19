a = int(input("From where do you want the natural numbers to start:\n"))
z = int(input("To where do you want the natural numbers:\n"))
c = 0
h = 0

print("Natural numbers:")
for n in range(a, z + 1):
    print(n)
    if n % 2 == 0:
        print(f"Even: {n}")

print("No more even numbers")

# Sum
for n in range(a, z + 1):
    c = c + n

print(f"The sum is: {c}")

# Squares
print("Squares:")
for n in range(a, z + 1):
    f = n * n
    print(f"The square is: {f}")

# Sum of squares
for n in range(a, z + 1):
    f = n * n
    h = h + f

print(f"The sum of squares is: {h}")
#factors
q=int(input("Enter the number you want to get the factors for: "))
for i in range(1,q+1):
    if q % i == 0:
        print(f"{i} is a factor of {q}")

#pattern square
ll=int(input("What is the number of rows you want: "))
for r in range (ll+1):
    for c in range (ll+1):
        if r == 0 or c == 0 or r == ll or c == ll:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#pattern triangle
for t in range(ll+1):
    for c in range(t+1):
        print("*", end=" ")  
    print()  
