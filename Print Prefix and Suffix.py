s = input()
for j in range(len(s)):
    prefix = s[: j + 1]
    print(prefix)
print()
for k in range(len(s) - 1, -1, -1):
    suffix = s[k:]
    print(suffix)
print()
