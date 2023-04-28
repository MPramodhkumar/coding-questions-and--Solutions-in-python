t=int(input())
for _ in range(t):
    
    n=int(input())
    arr = list(map(int, input().split()))
    maximum=arr[-1]
    res=[maximum]
    #iterate over the array from the right side to the left side
    for i in range(n-2,-1,-1):
        if arr[i]>=maximum:
            res.append(arr[i])
            maximum=arr[i]
    for leader in res:
        print(leader, end=" ")
    print()
          
