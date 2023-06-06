t = int(input())
while t > 0:
    Flag = True
    vowel = ["a", "e", "i", "o", "u"]
    string = input()
    for i in range(len(string) - 1):
        if string[i] != "n" and string[i] not in vowel:
            if string[i + 1] not in vowel:
                Flag = False
                break
    if string[len(string) - 1] != "n" and string[len(string) - 1] not in vowel:
        Flag = False
    if Flag:
        print("YES")
    else:
        print("NO")
    t = t - 1
