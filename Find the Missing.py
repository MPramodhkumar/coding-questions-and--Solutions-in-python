t=int(input())
for i in range(t):
  n=int(input())
  arr = list(map(int, input().split()))
  sum1 = n*(n+1)//2
  sum2=0
  for i in arr:
    if i!=0:
     sum2+=i
  print(sum1-sum2)
        
    
