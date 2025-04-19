a = int(input("Enter the number of rows you want: "))
arr = []


for i in range(a):
    b = int(input(f"Enter the element {i + 1} you want to be written in the row: "))#change the int in front to str for string 
    arr.append(b)


for j in range(a):
    for i in range(j + 1):
        print(arr[i], end=" ")
    print()
