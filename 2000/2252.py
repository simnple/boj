from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph_depth = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    front, back = map(int, input().split())
    graph[front].append(back)
    graph_depth[back] += 1

result = []

queue = deque()
for i in range(1, N + 1):
    if graph_depth[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()

    result.append(node)

    for i in graph[node]:
        graph_depth[i] -= 1
        if graph_depth[i] == 0:
            queue.append(i)

print(*result)