t = int(input())
for _ in range(t):
    n = int(input())
    houses = list(map(int, input().split()))
    minimum = min(houses)
    print(houses.index(minimum))
