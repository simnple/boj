from collections import deque

MOVEMENTS = (1, 2, 3, 4, 5, 6)
N, M = map(int, input().split())

board = [0] * (100 + 1)
snakes = [0] * (100 + 1)

for _ in range(N + M):
    x, y = map(int, input().split())
    snakes[x] = y

stack = deque([1])

while stack:
    pos = stack.popleft()

    for dx in MOVEMENTS:
        moved_pos = pos + dx

        while snakes[moved_pos]:
            moved_pos = snakes[moved_pos]

        if moved_pos >= 100:
            print(board[pos] + 1)
            exit()

        if board[moved_pos]: continue
        board[moved_pos] = board[pos] + 1

        stack.append(moved_pos)