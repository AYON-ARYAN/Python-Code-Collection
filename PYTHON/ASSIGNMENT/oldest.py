
people = []


for z in range(6):
    print(f"Enter details for person {z + 1}:")
    n= input("Name: ")
    a = int(input("Age: "))
    people.append({'name': n, 'age': a})


oldest_person = max(people, key=lambda x: x['age'])
youngest_person = min(people, key=lambda x: x['age'])


print("\nDetails of the oldest person:")
print(f"Name: {oldest_person['name']}")
print(f"Age: {oldest_person['age']}")

print("\nDetails of the youngest person:")
print(f"Name: {youngest_person['name']}")
print(f"Age: {youngest_person['age']}")
