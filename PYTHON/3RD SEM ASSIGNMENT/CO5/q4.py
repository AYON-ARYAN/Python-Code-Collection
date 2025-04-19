import math

def f(x):
    return math.sin(x)

def simpson(a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        result += f(x) * (4 if i % 2 else 2)
    return result * h / 3

print("Integral using Simpson's rule:", simpson(0, math.pi, 6))
print("Ayon_Aryan\n1RVU23CSE093")