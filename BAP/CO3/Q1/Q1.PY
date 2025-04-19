phonebook = {'John': "00903234561", 'Mary': "02359332865", 'Bill': "004934784530"}

def i():
    for key in phonebook.keys():
        print(f"The names are: {key}")

def ii():
    for value in phonebook.values():
        print(f"The numbers are: {value}")

def iii():
    for name, number in phonebook.items():
        print((name, number))

def iv():
    sorted_phonebook = sorted(phonebook.items())
    print("Alphabetically sorted telephone book:")
    for name, number in sorted_phonebook:
        print((name, number))

def v():
    n = "Mary"  # Hardcoding Mary for this option
    if n in phonebook:
        print(f"The number for {n} is: {phonebook[n]}")
    else:
        print(f"{n} not found in the phonebook.")

def vi():
    k = int(input("Enter the number of entries you want to make: "))
    for i in range(k):
        name = input("Enter the person's name: ")
        num = input("Enter the person's phone number: ")
        phonebook[name] = num

def vii():
    g = input("Enter the name you want to delete in the dictionary: ")
    if g in phonebook:
        print(f"{g} is deleted.")
        del phonebook[g]
    else:
        print(f"{g} not found in the phonebook.")

def viii():
    o = "John"  # Hardcoding John for this option
    if o in phonebook:
        print(f"{o} is found in the phonebook.")
    else:
        print(f"{o} is not found in the phonebook.")

# Menu driver program
while True:
    print("\nMenu:")
    print("1. Return all names of the phonebook")
    print("2. Return all phone numbers of the phonebook")
    print("3. Return all names and phone numbers in tuples")
    print("4. Alphabetically sort the telephone book")
    print("5. Ask for the phone number for Mary")
    print("6. Add new entries in the phonebook")
    print("7. Delete an entry")
    print("8. Check whether 'John' is in the phonebook")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        i()
    elif choice == 2:
        ii()
    elif choice == 3:
        iii()
    elif choice == 4:
        iv()
    elif choice == 5:
        v()
    elif choice == 6:
        vi()
    elif choice == 7:
        vii()
    elif choice == 8:
        viii()
    elif choice == 9:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
