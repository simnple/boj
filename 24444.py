from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N):
    graph[i].sort()

visited = [0] * (N + 1)
stack = deque([R])

count = 1
while stack:
    node = stack.popleft()

    if not visited[node]:
        visited[node] = count
        count += 1

        for i in graph[node]:
            if not visited[i]:
                stack.append(i)

print(*visited[1:], sep="\n")