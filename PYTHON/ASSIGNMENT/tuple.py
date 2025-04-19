a=input("Input user marks in the tuple seperated by commas: ")
turtle=tuple(a.split(","))
#sum
sum=0
for i in turtle:
    sum=sum+int(i)
print(f"The average is {sum}")
#average
average=sum/len(turtle)
print(f"The average is {average}")
#max value
max=turtle[0]
for i in turtle:
    if int(i)>int(max):
        max=i
print(f"The max value is {max}")
#min value
min=turtle[0]
for j in turtle:
    if int(j)<int(min):
        min=j
print(f"The min value is {min}")