observed = [8, 10, 9, 12, 11, 10]
expected = [10] * 6

chi_square = sum((o - e) ** 2 / e for o, e in zip(observed, expected))

print("Chi-Square:", chi_square)

critical_value = 11.07

if chi_square > critical_value:
    print("Reject null hypothesis.")
else:
    print("Fail to reject null hypothesis.")

print("Ayon_Aryan\n1RVU23CSE093")