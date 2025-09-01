import sys

def input(): return sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

stack = [R]
visited = [0] * (N + 1)

count = 1
while stack:
    node = stack.pop()

    if visited[node] == 0:
        visited[node] = count
        count += 1

        for i in graph[node]:
            if not visited[i]:
                stack.append(i)

print(*visited[1:], sep="\n")