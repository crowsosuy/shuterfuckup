n = int(input())
def cubesum(n):
    SUM = 0
    while n != 0:
        SUM += (n % 10)**3
        n //= 10
    return SUM
print

