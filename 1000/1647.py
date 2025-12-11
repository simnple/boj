import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

heap = [(0, 1)]

cost = 0
largest_cost = 0
left_nodes = N

while heap and left_nodes:
    curr_cost, curr_node = heapq.heappop(heap)

    if visited[curr_node]: continue

    visited[curr_node] = 1
    cost += curr_cost
    largest_cost = max(largest_cost, curr_cost)
    left_nodes -= 1

    for next_cost, next_node in graph[curr_node]:
        if visited[next_node]: continue

        heapq.heappush(heap, (next_cost, next_node))

print(cost - largest_cost)