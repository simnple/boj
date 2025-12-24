from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
start, end = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    
    graph[x].append(y)
    graph[y].append(x)

queue = deque([start])
visited = [-1] * (N + 1)
visited[start] = 0

while queue:
    node = queue.popleft()

    if node == end:
        break

    for i in graph[node]:
        if visited[i] != -1: continue

        visited[i] = visited[node] + 1
        queue.append(i)

print(visited[end])