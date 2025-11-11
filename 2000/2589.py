from collections import deque
import sys

input = sys.stdin.readline
diffs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

height, width = map(int, input().split())
box = [input().rstrip() for _ in range(height)]
maximum_duration = 0

for y in range(height):
    for x in range(width):
        if box[y][x] == "W": continue

        visited = [[-1] * width for _ in range(height)]
        visited[y][x] = 0
        queue = deque([(x, y)])
        value = 0

        while queue:
            node_x, node_y = queue.popleft()
            value = max(value, visited[node_y][node_x])

            for dx, dy in diffs:
                if not (0 <= node_x + dx < width and 0 <= node_y + dy < height): continue
                if box[node_y + dy][node_x + dx] == "W": continue
                if visited[node_y + dy][node_x + dx] != -1: continue

                visited[node_y + dy][node_x + dx] = visited[node_y][node_x] + 1
                queue.append((node_x + dx, node_y + dy))

        maximum_duration = max(maximum_duration, value)

print(maximum_duration)