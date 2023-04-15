def max_blocks(m, n):
    total_squares = m * n
    max_blocks = total_squares // 2
    return max_blocks
t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    print(max_blocks(m, n))
