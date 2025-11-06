import heapq
import sys

INF = float("inf")
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

cost = [INF] * (V + 1)
cost[K] = 0

graph = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

hq = []
heapq.heappush(hq, (0, K))

while hq:
    current_cost, start = heapq.heappop(hq)

    if current_cost > cost[start]: continue

    for i in range(len(graph[start])):
        end_cost, end = graph[start][i]

        total_cost = current_cost + end_cost

        if total_cost < cost[end]:
            cost[end] = total_cost
            heapq.heappush(hq, (total_cost, end))

for i in range(1, V + 1):
    if cost[i] == INF:
        print("INF")
    else:
        print(cost[i])