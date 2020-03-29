def sumOfNum():
    n = int(input())
    if n == 0:
        return 0
    return n + sumOfNum() - 1
print(sumOfNum())
