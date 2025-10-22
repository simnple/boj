from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

graph = {}

for _ in range(N-1):
    u, v = map(int, input().split())

    if not graph.get(u):
        graph[u] = [v]
    else:
        graph[u].append(v)

    if not graph.get(v):
        graph[v] = [u]
    else:
        graph[v].append(u)

nodes = [0] * (N + 1)
nodes[1] = 1

stacks = deque([1])

while stacks:
    node = stacks.popleft()

    for i in graph[node]:
        if not nodes[i]:
            nodes[i] = node
            stacks.append(i)

for i in range(2, N + 1):
    print(nodes[i])