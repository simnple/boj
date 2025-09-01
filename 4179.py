from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

MOVEMENTS = ((1, 0), (-1, 0), (0, 1), (0, -1))
R, C = map(int, input().split())

stack = deque()
board = [[] for _ in range(R)]
for i in range(R):
    data = list(input())
    for j in range(len(data)):
        if data[j] == "J":
            stack.append((False, j, i, 0))
            board[i].append(".")

        elif data[j] == "F":
            stack.append((True, j, i, 0))
            board[i].append(data[j])

        else:
            board[i].append(data[j])

stack = deque(sorted(stack, key=lambda x: int(x[0])))

while stack:
    is_fire, x, y, move_count = stack.popleft()

    if not is_fire:
        if board[y][x] == "J" or board[y][x] == "F": continue
        board[y][x] = "J"

    for dx, dy in MOVEMENTS:
        temp_x = x + dx
        temp_y = y + dy

        if not (0 <= temp_x <= C-1 and 0 <= temp_y <= R-1):
            if not is_fire:
                print(move_count + 1)
                exit()
            continue

        if board[temp_y][temp_x] == "#" or board[temp_y][temp_x] == "F": continue

        if not is_fire:
            if board[temp_y][temp_x] == "J": continue

        else:
            board[temp_y][temp_x] = "F"

        stack.append((is_fire, temp_x, temp_y, move_count + 1))

print("IMPOSSIBLE")