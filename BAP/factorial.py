def factorial():
  a = int(input("What is the number you want the factorial for: "))

  if a == 0:
    print("The factorial will not be there as the number is 0")
  else:
    c = 1  
    for b in range(1, a + 1):
      c *= b  
    print(f"The factorial is {c}")

factorial()
