n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    cnt1 = arr.count(i)
    if cnt1 <= 1:
        cnt += 1
    else:
        continue
print(cnt)
