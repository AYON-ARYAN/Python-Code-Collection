def q3(my_list):
    dictionary = {'less': 0, 'more': 0}

    for num in my_list:
        if num <= 0:
            dictionary['less'] += 1
        else:
            dictionary['more'] += 1

    return dictionary

my_list = []
more = 0
less = 0

a = int(input("Enter the number of elements you want in the list: "))
for i in range(a):
    b = int(input(f"Enter the element {i}: "))
    my_list.append(b)

result = q3(my_list)
print("Output:", result)
