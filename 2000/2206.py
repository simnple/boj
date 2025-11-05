from collections import deque
import sys

input = sys.stdin.readline
diffs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = map(int, input().split())
box = [list(map(int, input().rstrip())) for _ in range(N)]

stack = deque([(0, 0, 0)])
visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]
visited[0][0] = [1, 1]

while stack:
    x, y, is_skip = stack.popleft()

    if x == M - 1 and y == N - 1:
        print(visited[y][x][is_skip])
        sys.exit(0)

    for dx, dy in diffs:
        if not (0 <= x + dx < M and 0 <= y + dy < N): continue
        elif visited[y + dy][x + dx][is_skip] != -1: continue

        if box[y + dy][x + dx] == 1 and not is_skip:
            visited[y + dy][x + dx][True] = visited[y][x][is_skip] + 1
            stack.append((x + dx, y + dy, True))

        elif box[y + dy][x + dx] == 0:
            visited[y + dy][x + dx][is_skip] = visited[y][x][is_skip] + 1
            stack.append((x + dx, y + dy, is_skip))

print(-1)