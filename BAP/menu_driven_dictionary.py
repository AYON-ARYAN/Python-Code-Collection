dictionary={}
a=0
z=-1
while a==0:
    b=int(input("\nEnter the key value you want to happen in the dictionary\nPress 1 for adding key and value\n Press 2 for deleting key and value\n press 3 for deleting the last key and value\n press 4 for accesing the key and value\n Press 5 for display\n Press 6 for exit \n")
          )
    if b==1 :
        c=input("Enter the key: ")
        d=input("Enter the value: ")
        z+1
        dictionary[c]=d
    elif b==2:
        e=input("Enter the key: ")
        print(f"The key and value deleted {dictionary[e]}")
        dictionary.pop(e)
        z-1
    elif b==3:
        print(f"The element deleted ={dictionary[z]}")
        dictionary.popitem()
    elif b==4:
        f=input("Enter the key of the element you want to access: ")
        print(f"The key and value  is {dictionary[f]}")
    elif b==5:
        print(dictionary)
    elif b==6:
        print("Exitting........")
        a=1