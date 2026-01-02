from collections import deque
import sys

input = sys.stdin.readline
diffs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N = int(input())

box = []
queue = deque()
visited = [[-1] * N for _ in range(N)]
fishes = []
temp = []

baby_shark_size = 2
baby_shark_count = 0

for i in range(N):
    lines = list(map(int, input().split()))
    for j in range(N):
        if lines[j] == 9:
            queue.append((j, i))
            visited[i][j] = 0
            lines[j] = 0

    box.append(lines)

result = 0

while True:
    while queue:
        curr_x, curr_y = queue.popleft()

        for dx, dy in diffs:
            next_x, next_y = curr_x + dx, curr_y + dy
            if not (0 <= next_x < N and 0 <= next_y < N): continue
            if visited[next_y][next_x] != -1: continue
            if box[next_y][next_x] > baby_shark_size: continue

            visited[next_y][next_x] = visited[curr_y][curr_x] + 1

            if 0 < box[next_y][next_x] < baby_shark_size:
                fishes.append((next_x, next_y))
            else:
                temp.append((next_x, next_y))

    if fishes:
        new_x, new_y = sorted(fishes, key=lambda x: (x[1], x[0]))[0]
        result += visited[new_y][new_x]

        queue = deque([(new_x, new_y)])
        visited = [[-1] * N for _ in range(N)]
        fishes = []
        temp = []

        visited[new_y][new_x] = 0
        box[new_y][new_x] = 0

        baby_shark_count += 1
        if baby_shark_size == baby_shark_count:
            baby_shark_size += 1
            baby_shark_count = 0

    elif temp:
        for i in temp:
            queue.append(i)
        temp = []
    else:
        break

print(result)