my_list=[]
a=int (input("Enter the numbers of digit you want in the list"))
for c in range (0,a):
    b=int(input("Enter the element you want in the list: "))
    my_list.append(b)
for d in range (0,a):
    print(f"The element {d} is {my_list[d]}")

# squaring the elements
for e in range (0,a):
    print(f"The square of {my_list[e]} is {my_list[e]*my_list[e]}")    
# sum of all elements
sum=0
for f in range(0,a):
    sum+=my_list[f]
print(f"The sum of all elements is {sum}")


 
        