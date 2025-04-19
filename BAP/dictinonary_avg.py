#using the list
#list={68.8,70.2,67.2,71.8,73.2,75.6,74.0}
tlist = []

z = int(input("Enter the number of days you want: "))
dictionary = {}

for i in range(z):
    a = input("Enter the name of day: ")
    b = float(input("Enter the temperature: ")) 
    dictionary[a] = b

f = len(dictionary) 
g = 0

for temp in dictionary.values():  
    g += temp

avg = g / f

print(f"The avg is {avg}")


# for temp in dictionary.values():
#     if 70 <= temp <= 79:
#         tlist.append(temp)

# print(f"The list is {tlist}")


