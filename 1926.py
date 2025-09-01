from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
scales = []

for y in range(n):
    for x in range(m):
        stack = deque([(x, y)])
        if visited[y][x] or not pos[y][x]: continue

        scale = 0
        while stack:
            node_x, node_y = stack.pop()
            if not (0 <= node_x <= m-1) or not (0 <= node_y <= n-1): continue
            if visited[node_y][node_x] or not pos[node_y][node_x]: continue

            visited[node_y][node_x] = True
            scale += 1

            stack.append((node_x-1, node_y))
            stack.append((node_x+1, node_y))
            stack.append((node_x, node_y-1))
            stack.append((node_x, node_y+1))

        scales.append(scale)

print(len(scales))
print(max(scales) if scales else 0)