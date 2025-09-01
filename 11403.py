from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(N):
    data = list(map(int, input().split()))

    for j in range(len(data)):
        if data[j]:
            graph[i + 1].append(j + 1)

for i in range(1, N + 1):
    stack = deque([i])
    visited = [0] * (N + 1)

    while stack:
        node = stack.popleft()

        for j in graph[node]:
            if visited[j]: continue
            visited[j] = 1
            stack.append(j)

    print(*visited[1:])