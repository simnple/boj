import heapq
import sys

INF = float("inf")
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

start, end = map(int, input().split())

heap = [(0, start)]
visited = [INF] * (N + 1)
history = [0] * (N + 1)
visited[start] = 0
history[start] = start

while heap:
    curr_cost, curr_idx = heapq.heappop(heap)

    if curr_cost > visited[curr_idx]:
        continue

    for extra_cost, end_idx in graph[curr_idx]:
        if curr_cost + extra_cost >= visited[end_idx]: continue

        visited[end_idx] = curr_cost + extra_cost
        history[end_idx] = curr_idx

        heapq.heappush(heap, (curr_cost + extra_cost, end_idx))

print(visited[end])

result = [end]
value = end
while value != history[value]:
    value = history[value]
    result.append(value)

print(len(result))
print(*result[::-1])