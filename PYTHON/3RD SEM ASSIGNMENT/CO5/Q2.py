def f(x):
    return x**3 - 4*x + 1

def f_prime(x):
    return 3*x**2 - 4

def newton_raphson(x, n):
    for _ in range(n):
        x = x - f(x) / f_prime(x)
    return x

root = newton_raphson(1.5, 10)
print("Approximate root:", root)

print("Ayon_Aryan\n1RVU23CSE093")
