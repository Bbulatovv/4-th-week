def power(x, p):
    if p == 0:
        return 1
    elif p == 1:
        return x
    elif p % 2 != 0:
        return x * power(x, p - 1)
    elif p % 2 == 0:
        return power(x * x, p / 2)
x = float(input())
p = float(input())
print(power(x, p))
