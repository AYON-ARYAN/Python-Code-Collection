def f(x):
    return x**2 + 2*x + 1

def trapezoidal(a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

for n in [10, 20, 50]:
    print("Integral with", n, "subdivisions:", trapezoidal(1, 5, n))

print("Ayon_Aryan\n1RVU23CSE093")