from collections import deque
import sys

input = sys.stdin.readline
DIRECTIONS = ((1,2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1))

T = int(input())

for _ in range(T):
    l = int(input())
    knight_pos = tuple(map(int, input().split()))
    arrival_pos = tuple(map(int, input().split()))

    stack = deque([knight_pos])
    board = [[0] * l for _ in range(l)]

    while stack:
        x, y = stack.popleft()

        if arrival_pos == (x, y):
            print(board[y][x])
            break

        for dx, dy in DIRECTIONS:
            temp_x, temp_y = x + dx, y + dy

            if not (0 <= temp_x <= l-1 and 0 <= temp_y <= l-1): continue
            if not board[temp_y][temp_x]:
                board[temp_y][temp_x] = board[y][x] + 1
                stack.append((temp_x, temp_y))
