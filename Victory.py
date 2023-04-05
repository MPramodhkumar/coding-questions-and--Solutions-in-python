import math

t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    gcd = l
    for i in range(l+1, r+1):
        gcd = math.gcd(gcd, i)
    print(gcd)
