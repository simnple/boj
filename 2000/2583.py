import sys

input = sys.stdin.readline
diffs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

M, N, K = map(int, input().split())

visited = [[0] * N for _ in range(M)]
areas = []

for _ in range(K):
    x_1, y_1, x_2, y_2 = map(int, input().split())

    for y in range(y_1, y_2):
        for x in range(x_1, x_2):
            visited[y][x] = 1

for y in range(M):
    for x in range(N):
        if visited[y][x]: continue

        stack = [(x, y)]
        area = 0

        while stack:
            nx, ny = stack.pop()
            if visited[ny][nx]: continue
            
            visited[ny][nx] = 1
            area += 1
            
            for dx, dy in diffs:
                next_x, next_y = nx + dx, ny + dy

                if not (0 <= next_x < N and 0 <= next_y < M): continue
                if visited[next_y][next_x]: continue

                stack.append((next_x, next_y))
            
        areas.append(area)

print(len(areas))
print(*sorted(areas))