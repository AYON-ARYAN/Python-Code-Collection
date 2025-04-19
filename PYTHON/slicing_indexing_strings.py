string =str(input("Enter a string: "))
print(string[1])
a=int(input("From which index you want to slice the string: "))
b=int(input("To which index you want to slice the string: "))
print(string[a:b])
c=int(input("What is number gap you want in the string: "))
print(string[::c])
# string[start:stop:step]
print(f"Reversed string:{string[::-1]}")