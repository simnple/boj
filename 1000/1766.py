import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    front, back = map(int, input().split())
    in_degree[back] += 1
    graph[front].append(back)

heap = []
for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    node = heapq.heappop(heap)
    result.append(node)

    for i in graph[node]:
        in_degree[i] -= 1

        if in_degree[i] == 0:
            heapq.heappush(heap, i)

print(*result)