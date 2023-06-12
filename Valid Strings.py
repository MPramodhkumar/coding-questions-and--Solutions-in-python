t = int(input())
while t > 0:
    str = input()
    leng = len(str)
    count = 0
    count1 = 0
    if leng % 2 == 0:
        for i in range(leng):
            ch = str[i]
            if ch == "(":
                count += 1
            elif ch == ")":
                count -= 1
            count1 = min(count, count1)
        if count1 < -1 or count > 0:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
    t = t - 1
