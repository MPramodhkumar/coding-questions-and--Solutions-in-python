m, n = map(int, input().split())
mat1 = []
for i in range(m):
    mat1.append(list(map(int, input().split())))
mat2 = []
for i in range(m):
    mat2.append(list(map(int, input().split())))
mat3 = []
for i in range(m):
    mat3.append([0] * m)

for i in range(m):
    for j in range(n):
        mat3[i][j] = mat1[i][j] + mat2[i][j]
mat4 = []
for i in range(m):
    mat4.append([0] * m)
for i in range(m):
    for j in range(n):
        for k in range(n):
            mat4[i][j] = mat4[i][j] + mat1[i][k] * mat2[k][j]
for i in range(m):
    for j in range(n):
        print(mat3[i][j], end=" ")
    print()
for i in range(m):
    for j in range(n):
        print(mat4[i][j], end=" ")
    print()
