from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph_depth = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A = list(map(int, input().split()))
    if A[0] < 2: continue
    
    for i in range(1, A[0]):
        front, back = A[i], A[i + 1]
        graph[front].append(back)
        graph_depth[back] += 1

queue = deque()
for i in range(1, N + 1):
    if graph_depth[i] == 0:
        queue.append(i)

result = []
while queue:
    node = queue.popleft()
    result.append(node)

    for i in graph[node]:
        graph_depth[i] -= 1
        if graph_depth[i] == 0:
            queue.append(i)

if len(result) == N:
    print(*result, sep="\n")
else:
    print(0)