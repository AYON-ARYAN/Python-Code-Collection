a = [67, 45, 98, 45, 23, 45, 87]
b = []

for item in a:
    if item not in b:
        b.append(item)

print("Original List:", a)
print("List without Duplicates:", b)
