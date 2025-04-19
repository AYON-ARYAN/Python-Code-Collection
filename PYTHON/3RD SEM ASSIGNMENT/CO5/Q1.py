def f(x):
    return x**3 - 4*x - 9

def bisection(a, b, n):
    for _ in range(n):
        mid = (a + b) / 2
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return mid

root = bisection(2, 3, 10)
print("Approximate root:", root)

print("Ayon_Aryan\n1RVU23CSE093")
