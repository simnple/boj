from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

graph = {i: [] for i in range(1, N+1)}
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (N+1)

for start in range(1, N+1):
    if visited[start]: continue
    stack = deque([start])
    visited[start] = True

    while stack:
        node = stack.pop()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
    count += 1

print(count)