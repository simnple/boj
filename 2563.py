board = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())
for _ in range(N):
    L, D = map(int, input().split())
    for y in range(D, D+10):
        for x in range(L, L+10):
            board[y][x] = 1

result = 0
for l in board:
    result += sum(l)
print(result)