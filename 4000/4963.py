import sys

input = sys.stdin.readline
diffs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]

while True:
    w, h = map(int, input().split())
    if w == h == 0: break

    visited = [[False] * w for _ in range(h)]
    box = [list(map(int, input().split())) for _ in range(h)]

    island = 0

    for y in range(h):
        for x in range(w):
            if box[y][x] == 1 and not visited[y][x]:
                stack = [(x, y)]

                while stack:
                    node_x, node_y = stack.pop()
                    
                    if not visited[node_y][node_x]:
                        visited[node_y][node_x] = True

                        for dx, dy in diffs:
                            if not (0 <= node_x + dx < w and 0 <= node_y + dy < h): continue
                            if visited[node_y + dy][node_x + dx]: continue
                            if box[node_y + dy][node_x + dx] == 0: continue

                            stack.append((node_x + dx, node_y + dy))

                island += 1
    
    print(island)