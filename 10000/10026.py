import sys

def input(): return sys.stdin.readline().rstrip()

MOVEMENTS = ((1, 0), (-1, 0), (0, 1), (0, -1))
N = int(input())

color = [list(input()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
three_color_count = {"R": 0, "G": 0, "B": 0}
for y in range(N):
    for x in range(N):
        if visited[y][x]: continue
        stack = [(x, y)]
        visited[y][x] = True

        while stack:
            node_x, node_y = stack.pop()

            for dx, dy in MOVEMENTS:
                temp_x = node_x + dx
                temp_y = node_y + dy

                if not (0 <= temp_x <= N-1 and 0 <= temp_y <= N-1): continue
                if visited[temp_y][temp_x]: continue
                if color[node_y][node_x] != color[temp_y][temp_x]: continue

                visited[temp_y][temp_x] = True
                stack.append((temp_x, temp_y))

        three_color_count[color[y][x]] += 1

visited = [[False] * N for _ in range(N)]
two_color_count = {"RG": 0, "B": 0}
for y in range(N):
    for x in range(N):
        if visited[y][x]: continue
        stack = [(x, y)]
        color_name = "RG" if color[y][x] != "B" else "B"

        while stack:
            node_x, node_y = stack.pop()

            for dx, dy in MOVEMENTS:
                temp_x = node_x + dx
                temp_y = node_y + dy

                if not (0 <= temp_x <= N-1 and 0 <= temp_y <= N-1): continue
                if visited[temp_y][temp_x]: continue

                temp_color_name = "RG" if color[temp_y][temp_x] != "B" else "B"
                if color_name != temp_color_name: continue

                visited[temp_y][temp_x] = True
                stack.append((temp_x, temp_y))

        two_color_count[color_name] += 1

print(sum(three_color_count.values()), sum(two_color_count.values()))