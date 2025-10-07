import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

input()
N = int(input())

graph = {}

for _ in range(N):
    start, end = map(int, input().split())
    if start not in graph:
        graph[start] = [end]
    elif end not in graph[start]:
        graph[start].append(end)

    if end not in graph:
        graph[end] = [start]
    elif start not in graph[end]:
        graph[end].append(start)

visited = set()
queue = deque([1])

while queue:
    n = queue.popleft()
    if n not in visited:
        visited.add(n)
        if n in graph:
            queue.extend(sorted(set(graph[n]) - visited))

print(len(visited) - 1)