m, n = map(int, input().split())
mat1 = []
for i in range(m):
    mat1.append(list(map(int, input().split())))
lower_triangle = [[0] * n for _ in range(m)]
upper_triangle = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(m):
        if i >= j:
            lower_triangle[i][j] = mat1[i][j]
        if i <= j:
            upper_triangle[i][j] = mat1[i][j]
for i in range(m):
    for j in range(n):
        print(lower_triangle[i][j], end=" ")
    print()
for i in range(m):
    for j in range(n):
        print(upper_triangle[i][j], end=" ")
    print()
