from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
time = [0] * (N + 1)

graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for i in range(1, N + 1):
    D = list(map(int, input().split()))
    time[i] = D[0]

    for j in range(1, len(D)):
        if D[j] == -1: break

        graph[D[j]].append(i)
        in_degree[i] += 1

queue = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)

result = time[:]
while queue:
    node = queue.pop()

    for i in graph[node]:
        in_degree[i] -= 1
        result[i] = max(result[i], result[node] + time[i])
        
        if in_degree[i] == 0:
            queue.append(i)

print(*result[1:], sep="\n")