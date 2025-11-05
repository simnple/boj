import sys

input = sys.stdin.readline
diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
box = [list(map(int, input().split())) for _ in range(N)]

max_count = 0
for i in range(101):
    real_box = [[False] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            real_box[j][k] = box[j][k] > i

    visited = [[False] * N for _ in range(N)]
    count = 0
    for j in range(N):
        for k in range(N):
            if real_box[j][k] == False: continue
            elif visited[j][k]: continue

            stack = [(k, j)]

            while stack:
                x, y = stack.pop()

                if not visited[y][x]:
                    visited[y][x] = True

                    for dx, dy in diffs:
                        if not (0 <= x + dx < N and 0 <= y + dy < N): continue
                        elif visited[y + dy][x + dx]: continue
                        elif real_box[y + dy][x + dx] == False: continue

                        stack.append((x + dx, y + dy))

            count += 1

    max_count = max(max_count, count)

print(max_count)