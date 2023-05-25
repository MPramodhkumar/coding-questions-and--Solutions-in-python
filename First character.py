t = int(input())
while t > 0:
    word = input()
    Seen = []
    Unseen = []
    for i in word:
        if i in Unseen:
            Unseen.remove(i)
        elif i not in Seen:
            Seen.append(i)
            Unseen.append(i)
    if len(Unseen) > 0:
        first_elelment = Unseen[0]
        index = word.index(first_elelment)
        print(index)
    else:
        print("-1")
    t = t - 1
