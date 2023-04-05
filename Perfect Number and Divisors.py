k = int(input(""))
for i in range(k):
  n=int(input())
  sum1 = 0
  for i in range(1, n):
      if(n % i == 0):
          sum1 = sum1 + i
  if (sum1 == n):
      print("true")
  else:
      print("false")
