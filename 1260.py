from collections import deque

def dfs(start):
    visited = []
    stack = deque([start])

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))
    return visited

def bfs(start):
    visited = []
    stack = deque([start])

    while stack:
        node = stack.popleft()

        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node]))
    return visited

N, M, V = map(int, input().split())
graph = dict()

for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    start, end = map(int, input().split())
    if end not in graph[start]:
        graph[start].append(end)
    if start not in graph[end]:
        graph[end].append(start)

print(*dfs(V))
print(*bfs(V))