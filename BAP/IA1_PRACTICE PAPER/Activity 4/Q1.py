a = int(input("How many things you want to enter: ")) 
b = []

# Input loop
for i in range(a):
    c = input("Enter the things you want to enter in the list: ")
    b.append(c) 


unique_list = []
for item in b:
    if item not in unique_list:
        unique_list.append(item)


print(f"The list entered is: {unique_list}\nHaving {len(unique_list)} elements.")
