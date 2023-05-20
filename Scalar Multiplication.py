m, n, k = map(int, input().split())
mat1 = []
mat2 = []
for i in range(m):
    mat1.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        mat2.append(mat1[i][j] * k)
for i in range(len(mat2)):
    print(mat2[i], end=" ")
    if (i + 1) % n == 0:
        print()
