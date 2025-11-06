import heapq
import math
import sys

INF = float("inf")
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

def dijkstra(s, s_value, e):
    if s_value == INF:
        return [INF for i in e]
    cost = [INF] * (N + 1)
    cost[s] = s_value

    hq = []
    heapq.heappush(hq, (s_value, s))

    while hq:
        start_cost, start = heapq.heappop(hq)

        if start_cost > cost[start]: continue

        for i in range(len(graph[start])):
            end_cost, end = graph[start][i]

            total_cost = start_cost + end_cost

            if total_cost < cost[end]:
                cost[end] = total_cost
                heapq.heappush(hq, (total_cost, end))

    return [cost[i] for i in e]

cost_v1, cost_v2 = dijkstra(1, 0, [v1, v2])
cost_v1_v2, cost_v1_N = dijkstra(v1, cost_v1, [v2, N])
cost_v2_v1, cost_v2_N = dijkstra(v2, cost_v2, [v1, N])

min_value = min(cost_v1_v2 + cost_v2_N - cost_v2, cost_v2_v1 + cost_v1_N - cost_v1)
if min_value == INF or math.isnan(min_value): min_value = -1

print(min_value)