t = int(input())
for i in range(t):
    n, q = map(int, input().split())
    String = input()
    freq_arr = [0] * 26
    for i in String:
        freq_arr[ord(i) - 97] += 1
    for i in range(q):
        centers = int(input())
        count = 0
        for j in range(26):
            if freq_arr[j] > centers:
                count += freq_arr[j] - centers
        print(count)
