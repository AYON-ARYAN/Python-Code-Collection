a = int(input("What is the number of elements you want in the list? "))
my_list = [] 
rem=[]
for i in range(a):
    l = int(input(f"Enter the element {i + 1}: "))  
    my_list.append(l)  

print("The list you entered:", my_list)

# adding elements in the list
b=0
for i in range(a):
    b += my_list[i]

print(f"Sum of the elements in the list {b}")    
#multiplying elements in the list
c=1
for i in range(a):
    c *= my_list[i]

print(f"Product of the elements in the list {c}")
#even and odd elements in the list
odd=[]
even=[]
for i in range(a):
    if my_list[i] % 2 == 0:
        even.append(my_list[i])
    else:
        odd.append(my_list[i])
print(f"The odd elements are {odd}")        
print(f"The even elements are {even}")    
# copy elements from old to new list
rem=my_list.copy()
#remove elements from ths list    
X=int(input("How many elements do you want to delete from the list?"))
for i in range(X):
    z=int(input(f"Enter the element {i+1} you want to delete from the list: "))
    for i in range(a):
        if my_list[i] == z:
            rem.pop(i)
print(f"The list after removing the element {z} is {rem}")
#sorting all lists
rem.sort()
even.sort()
odd.sort()
my_list.sort()

print(f"The list after sorting is {my_list}")
print(f"The even list after sorting is {even}")
print(f"The odd list after sorting is {odd }")
print(f"The rem list after sorting is {rem}")