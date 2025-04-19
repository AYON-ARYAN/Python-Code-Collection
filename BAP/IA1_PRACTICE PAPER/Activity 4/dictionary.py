#the values cannot be duplicate in dictionary
dictionary={}
a=int(input("Enter the number of values you want in the dictionary: "))
for i in range(0,a):
    b=input("Enter the key value in the dictionary: ")
    c=input("Enter the value: ")
    dictionary[b]=c
    
print(dictionary)#prints the whole dictionary
#it is keys are like index
#it is values are like real values

print(dictionary.keys())#prints the keys.keys()
print(dictionary.values())#prints the values.values()
d=input("Enter the key of the element you want to delete: ")
dictionary.pop(d)#deletes the elements
#use popitem() to delete the last element of the dictionary  
#use del(dictionary name) for deleting the whole dictionary all at once
