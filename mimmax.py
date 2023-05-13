t = int(input())
for _ in range(t):
    n = int(input())
    elements = list(map(int, input().split()))
    min_element, max_element = min(elements), max(elements)
    print(min_element, max_element)
