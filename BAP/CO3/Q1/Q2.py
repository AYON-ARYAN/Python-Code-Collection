table = {
    '0': '000',
    '1': '001',
    '2': '010',
    '3': '011',
    '4': '100',
    '5': '101',
    '6': '110',
    '7': '111'
}


octal_number = input("Enter an octal number: ")


binary_number = ''
for digit in octal_number:
    binary_number +=table[digit]


print("Binary representation:", binary_number)
