a = float(input("Enter the number of days you have the book with you for late submission: "))
if a<=5:
    print(f"Your fine is: {a*0.50} Rs")
elif a in range (6,10):
    print(f"Your fine is: {a*1} Rs")

elif a>=10:
    print(f"Your fine is: {a*5} Rs")

elif a>=30:
    print("Sorry!, Your membership is cancelled.")

else:
    print("Enter a valid ay count!")
