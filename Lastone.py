t = int(input())
for _ in range(t):
    n = int(input())
    elements = list(map(int, input().split()))
    if 1 not in elements:
        print("-1")
    else:
       last_index = len(elements) - elements[::-1].index(1) - 1
       print(last_index)
    
