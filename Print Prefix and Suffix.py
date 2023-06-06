s = input()
prefixes = []
prefix = ""
for i in s:
    prefix += i
    prefixes.append(prefix)
suffixes = []
suffix = ""
for j in reversed(s):
    suffix += j
    suffixes.append(suffix)

for i in prefixes:
    print(i)


for j in suffixes:
    print(j)
