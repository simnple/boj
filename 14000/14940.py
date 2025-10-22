from collections import deque

n, m = map(int, input().split())

pos = [[] for _ in range(n)]
start_pos = [-1, -1]
for i in range(n):
    pos[i] = list(map(int, input().split()))
    if start_pos == [-1, -1] and 2 in pos[i]:
        start_pos = [pos[i].index(2), i]

visited = [[False for __ in range(m)] for _ in range(n)]
result = [[0 for __ in range(m)] for _ in range(n)]
stack = deque([[start_pos]])

for y in range(n):
    for x in range(m):
        if pos[y][x] == 0:
            visited[y][x] = True

count = 0
while stack[0] != []:
    node = stack.popleft()
    temp = []

    for x, y in node:
        if pos[y][x] == 0 or visited[y][x]: continue
        visited[y][x] = True

        if x-1 > -1: temp.append([x-1, y])
        if x+1 < m: temp.append([x+1, y])
        if y-1 > -1: temp.append([x, y-1])
        if y+1 < len(pos): temp.append([x, y+1])

    for x1, y1 in temp:
        if visited[y1][x1] or pos[y1][x1] == 0: continue
        result[y1][x1] = count + 1
    stack.append(temp)

    count += 1

for y in range(n):
    for x in range(m):
        if pos[y][x] == 1 and not visited[y][x]:
            result[y][x] = -1
    print(*result[y])