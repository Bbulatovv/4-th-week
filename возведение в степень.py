def power(a, n):
    if n == 0:
        return 1
    agusha = power(a * a, n // 2)
    if n % 2:
        agusha *= a
    return agusha
a = float(input())
n = float(input())
print(power(a, n))
