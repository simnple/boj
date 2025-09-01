from collections import deque
import sys

input = sys.stdin.readline

DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1))

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]

count = 0

stack = deque()
temp_stack = []
for h in range(H):
    for y in range(N):
        for x in range(M):
            if box[h][y][x] != 1: continue
            temp_stack.append((x, y, h))

stack.append(temp_stack)

while stack:
    node = stack.popleft()

    temp_stack = []
    for x, y, h in node:
        for dx, dy, dh in DIRECTIONS:
            temp_x, temp_y, temp_h = x + dx, y + dy, h + dh
            if not (0 <= temp_x <= M-1 and 0 <= temp_y <= N-1 and 0 <= temp_h <= H-1): continue
            if box[temp_h][temp_y][temp_x] != 0: continue

            box[temp_h][temp_y][temp_x] = 1
            temp_stack.append((temp_x, temp_y, temp_h))

    if temp_stack:
        stack.append(temp_stack)
        count += 1

for h in range(H):
    for y in range(N):
        for x in range(M):
            if box[h][y][x] == 0:
                print(-1)
                exit()

print(count)