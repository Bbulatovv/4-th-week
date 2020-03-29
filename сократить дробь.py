def ReduceFraction(n, m):
    Z1 = max(n, m)
    Z2 = min(n, m)
    if Z1 == Z2 and Z1 * Z2 != 0:
        return 1, 1
    else:
        Z = Z1 % Z2
        while Z > 0:
            Z1 = Z2
            Z2 = Z
            Z = Z1 % Z2
        return n // Z2, m // Z2
n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
