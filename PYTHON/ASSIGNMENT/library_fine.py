a=-int(input("Enter the number of days you were having book for?"))
if a<5:
    c=a*0.50
    print(f"Your fine would be ={c}")
elif a in range (6,10):
    c=a*1
    print("Your fine would be ={c}")
elif a in range (10,30):
    c=a*5
    print("Your fine would be ={c}")
elif a>30:
    print(f"Sorry your subscription have been terminated for because you submitted the book after {a} days.")
else:
    print("enter the valid number of days.")