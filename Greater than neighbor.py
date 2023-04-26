t = int(input())
for _ in range(t):
    n = int(input())
    elements = list(map(int, input().split()))
    res=[]
    if elements[0]>elements[1]:
        res.append(0)
    for i in range(1,n-1):
        if elements[i] > elements[i-1] and elements[i] > elements[i+1]:
            res.append(i)
       
    if elements[n-1]>elements[n-2]:
        res.append(n-1)
    if len(res)==0:
        res.append("-1")
   
    print(*res)
