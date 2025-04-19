def show_numbers(a):
    for i in range(a + 1):
        if i % 2 == 0:
            print(f"{i} Is Even")
        else:
            print(f"{i} Is Odd")    
        
a = int(input("Enter the number for checking: "))
show_numbers(a)
