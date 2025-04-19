a = int(input("Enter the number of rows: "))

# Print upper half of the pattern
for i in range(1, a + 1):
    for j in range(1, i + 1):
        if j == i:
            print(i, end='')
        else:
            print(f"{i}*", end='')
    print()

# Print lower half of the pattern
for i in range(a, 0, -1):
    for j in range(1, i + 1):
        if j == i:
            print(i, end='')
        else:
            print(f"{i}*", end='')
    print()
