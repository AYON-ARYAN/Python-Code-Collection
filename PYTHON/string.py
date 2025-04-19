a = str(input("Enter the string you want to concatenate: "))
b = int(input("Enter the index of letter from where you want to concatenate: "))
c = str(input("Enter the string you want to you want to concatenate to: "))

d=a[:b]
e=d+c
print(f"The new string is:\n {e}")
print(f"The split of the string is:\n {e.split()}")
print(f"To upper case the string use {e.upper()}")
print(f"To lower case the string use {e.lower()}")