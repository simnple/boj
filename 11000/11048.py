import sys

input = sys.stdin.readline
diffs = [(-1, 0), (0, -1), (-1, -1)]

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * (M + 1) for _ in range(N + 1)]
visited[1][1] = box[0][0]

for y in range(N):
    for x in range(M):
        for dx, dy in diffs:
            if not (0 <= x + dx < M and 0 <= y + dy < N): continue
            visited[y + 1][x + 1] = max(visited[y + 1][x + 1], box[y][x] + visited[y + dy + 1][x + dx + 1])

print(visited[N][M])