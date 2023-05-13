t=int(input())
for _ in range(t):
  n=int(input())
  arr=list(map(int, input().split()))
  maximum=len(arr)-1
  minimum=0
  lst = [0 for _ in range(n)]
  for i in range(len(arr)):
    if i%2==0:
      lst[i]=arr[maximum]
      maximum-=1
    else:
      lst[i]=arr[minimum]
      minimum+=1
  print(*lst)
