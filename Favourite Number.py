def FavouriteNumber(num):
    num=[int(i) for i in str(num)]
    cnt=0
    for i in num:
        if i==5:
            cnt+=1
    print(int(cnt))
t=int(input())
while t>0:
  FavouriteNumber(int(input()))
  t-=1
