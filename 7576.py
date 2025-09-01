from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

M, N = map(int, input().split())

box = []
empty_tomato = 0

for _ in range(N):
    data = list(map(int, input().split()))
    empty_tomato += data.count(-1)
    box.append(data)

visited = [[False] * M for _ in range(N)]
stack = deque([])

for y in range(N):
    for x in range(M):
        if box[y][x] != 1: continue
        stack.append((x, y, 0))

while stack:
    node_x, node_y, temp_day = stack.popleft()

    if not (0 <= node_x <= M-1) or not (0 <= node_y <= N-1): continue
    if visited[node_y][node_x] or box[node_y][node_x] < 0: continue

    visited[node_y][node_x] = True
    box[node_y][node_x] = 1

    stack.append((node_x-1, node_y, temp_day + 1))
    stack.append((node_x+1, node_y, temp_day + 1))
    stack.append((node_x, node_y-1, temp_day + 1))
    stack.append((node_x, node_y+1, temp_day + 1))

if sum([sum(line) for line in box]) == M * N - empty_tomato * 2:
    print(temp_day - 1)
else:
    print(-1)