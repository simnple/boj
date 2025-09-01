from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
pos = [list(map(int, list(input()))) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
stack = deque([[0, 0, 1]])
result = set()

while stack:
    node_x, node_y, count = stack.popleft()

    if node_x == M-1 and node_y == N-1:
        result.add(count)
        continue

    if not (0 <= node_x <= M - 1) or not (0 <= node_y <= N - 1): continue
    if not pos[node_y][node_x] or visited[node_y][node_x]: continue
    visited[node_y][node_x] = True

    stack.append([node_x-1, node_y, count+1])
    stack.append([node_x+1, node_y, count+1])
    stack.append([node_x, node_y-1, count+1])
    stack.append([node_x, node_y+1, count+1])

print(min(result))