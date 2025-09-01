from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

MOVEMENTS = ((1, 0), (-1, 0), (0, 1), (0, -1))

T = int(input())

for _ in range(T):
    w, h = map(int, input().split())

    result = "IMPOSSIBLE"
    stack = deque()
    board = [[] for _ in range(h)]
    for i in range(h):
        data = list(input())
        for j in range(len(data)):
            if data[j] == "@":
                stack.append((False, j, i, 0))
                board[i].append(".")

            elif data[j] == "*":
                stack.append((True, j, i, 0))
                board[i].append(data[j])

            else:
                board[i].append(data[j])

    stack = deque(sorted(stack, key=lambda x: int(x[0])))

    is_end = False
    while stack and not is_end:
        is_fire, x, y, move_count = stack.popleft()

        if not is_fire:
            if board[y][x] == "@" or board[y][x] == "*": continue
            board[y][x] = "@"

        for dx, dy in MOVEMENTS:
            temp_x = x + dx
            temp_y = y + dy

            if not (0 <= temp_x <= w-1 and 0 <= temp_y <= h-1):
                if not is_fire:
                    result = move_count + 1
                    is_end = True
                    break
                continue

            if board[temp_y][temp_x] == "#" or board[temp_y][temp_x] == "*": continue

            if not is_fire:
                if board[temp_y][temp_x] == "@": continue

            else:
                board[temp_y][temp_x] = "*"

            stack.append((is_fire, temp_x, temp_y, move_count + 1))

    print(result)