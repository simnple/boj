from itertools import combinations

N, M = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]
diffs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

safe_zoon = 0
max_safe_zoon = 0
stack = []
empty_space = []

for i in range(N):
    for j in range(M):
        if box[i][j] == 2:
            stack.append((j, i))
        elif box[i][j] == 0:
            empty_space.append((j, i))
            safe_zoon += 1

for wall in combinations(empty_space, 3):
    copy_safe_zoon = safe_zoon - 3
    copy_stack = stack.copy()
    visited = [[0] * M for _ in range(N)]

    while copy_stack:
        x, y = copy_stack.pop()

        if not visited[y][x]:
            visited[y][x] = 1

            if box[y][x] == 0: copy_safe_zoon -= 1

            for dx, dy in diffs:
                if (0 <= x + dx < M and 0 <= y + dy < N) and box[y + dy][x + dx] == 0 and (not visited[y + dy][x + dx]) and ((x + dx, y + dy) not in wall):
                    copy_stack.append((x + dx, y + dy))

    max_safe_zoon = max(max_safe_zoon, copy_safe_zoon)

print(max_safe_zoon)