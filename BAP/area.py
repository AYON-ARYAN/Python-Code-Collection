a = int(input("Choose a shape you want to get the area of (1) Rectangle, (2) Right Angle Triangle, (3) Square ,(4) Circle: "))

if a == 1:
    b = int(input("What is the length: "))
    c = int(input("What is the breadth: "))
    print(f"The area is {b * c}")

if a == 2:
    d = int(input("What is the base: "))
    e = int(input("What is the height: "))
    ans = 0.5 * d * e
    print(f"The area is {ans}")

if a == 3:
    f = int(input("What is the length: "))
    print(f"The area is {f**2}")

if a == 4:
    g = int(input("What is the radius: "))
    print(f"The area is {3.14 * g**2 }")

else:
    print("You need to enter the number which is written near to the shape ")
