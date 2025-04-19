# route = []

# rel = int(input("Are you a customer or an operator?\nPress 1 for customer\nPress 0 for operator\n: "))

# if rel == 0:
#     a = int(input("Do you want to add routes in the system?\nYes: Enter 1\nNo: Enter 0\n: "))
#     if a == 1:
#         b = int(input("Enter the number of bus routes you want to add: "))
#         for i in range(b):
#             c = str(input("Enter Route Destination: "))
#             route.append(c)
#         print("Routes added successfully!")
#     else:
#         print("No routes added.")

# elif rel == 1:
#     print("\nWelcome Customer")
#     print("Available routes:", route)
#     r = str(input("Enter the place you want to go to: "))
    
#     if r not in route:
#         print("Tickets are not available for this destination, Sorry!")
#     else:
#         print("Tickets available for this route.")
#         time = int(input("Enter the time you want the tickets for (Enter in 24 Hour format, e.g., 1245 for 12:45): "))
#         seat = int(input("Enter the seat number you want to book: "))
#         cos = int(input("Enter the number of tickets you want: "))
        
#         print("Congratulations, Your tickets have been booked!")
#         print(f"Seat Numbers: {seat} - {seat + cos - 1}")
#         print(f"Number of Passengers: {cos}")
#         print(f"Total Price: {200 * cos}")

#         print("\nUpdating route details...")
#         print("Adding and Updating Route details: ")
#         print("The application includes functionality to add and update the details of existing bus routes, ensuring accuracy and relevance.")

#         print("Generating E-Tickets...")
#         print("Upon successful booking, the system dynamically generates electronic tickets containing details such as the booked route, departure time, seat assignment, and fare.")
route = []

while True:
    print("\nMenu:")
    print("1. Customer")
    print("2. Operator")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nWelcome Customer")
        if len(route) == 0:
            print("No routes available.")
            continue

        print("Available routes:", route)
        r = str(input("Enter the place you want to go to: "))
        
        if r not in route:
            print("Tickets are not available for this destination, Sorry!")
        else:
            print("Tickets available for this route.")
            time = int(input("Enter the time you want the tickets for (Enter in 24 Hour format, e.g., 1245 for 12:45): "))
            seat = int(input("Enter the seat number you want to book: "))
            cos = int(input("Enter the number of tickets you want: "))
            
            print("Congratulations, Your tickets have been booked!")
            print(f"Seat Numbers: {seat} - {seat + cos - 1}")
            print(f"Number of Passengers: {cos}")
            print(f"Total Price: {200 * cos}")

    elif choice == 2:
        print("\nOperator Menu:")
        print("1. Add Routes")
        print("2. View Routes")
        print("3. Exit Operator Menu")

        operator_choice = int(input("Enter your choice: "))

        if operator_choice == 1:
            b = int(input("Enter the number of bus routes you want to add: "))
            for i in range(b):
                c = str(input("Enter Route Destination: "))
                route.append(c)
            print("Routes added successfully!")
        elif operator_choice == 2:
            print("Available routes:", route)
        elif operator_choice == 3:
            continue

    elif choice == 3:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please choose again.")
