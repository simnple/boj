import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

heap = []
visited = [0] * (V + 1)

smallest_weight = 2_147_483_647
smallest_graph = ()

for _ in range(E):
    A, B, C = map(int, input().split())
    if C < smallest_weight:
        smallest_weight = C
        smallest_graph = (A, B)

    graph[A].append((B, C))
    graph[B].append((A, C))

cost = smallest_weight
visited[smallest_graph[0]] = 1
visited[smallest_graph[1]] = 1

for i in smallest_graph:
    for node, weight in graph[i]:
        if visited[node]: continue
        heapq.heappush(heap, (weight, node))

while heap:
    curr_weight, curr_node = heapq.heappop(heap)

    if visited[curr_node]: continue
    visited[curr_node] = 1
    cost += curr_weight

    for next_node, next_weight in graph[curr_node]:
        if visited[next_node]: continue
        heapq.heappush(heap, (next_weight, next_node))

print(cost)