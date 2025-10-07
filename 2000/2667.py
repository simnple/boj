from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
pos = [list(map(int, list(input()))) for _ in range(N)]

visited = [[0 for _ in range(N)] for __ in range(N)]
rooms = []

for y in range(N):
    for x in range(N):
        if visited[y][x] or not pos[y][x]: continue
        rooms.append(0)

        stack = deque([(x, y)])

        count = 0
        while stack:
            node_x, node_y = stack.popleft()
            if not (0 <= node_x <= N - 1) or not (0 <= node_y <= N - 1): continue
            elif visited[node_y][node_x] or not pos[node_y][node_x]: continue
            visited[node_y][node_x] = True
            count += 1

            stack.append((node_x-1, node_y))
            stack.append((node_x+1, node_y))
            stack.append((node_x, node_y-1))
            stack.append((node_x, node_y+1))

        rooms[-1] = count

print(len(rooms))
for i in sorted(rooms):
    print(i)