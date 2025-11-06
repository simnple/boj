import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

INF = float("inf")
price_table = [INF] * (N + 1)
graph = {i: [] for i in range(N + 1)}

for _ in range(M):
    start, end, price = map(int, input().split())
    graph[start].append((end, price))

final_start, final_end = map(int, input().split())
price_table[final_start] = 0

heap = []
heapq.heappush(heap, (0, final_start))

while heap:
    current_price, start = heapq.heappop(heap)

    if price_table[start] < current_price: continue

    for i in range(len(graph[start])):
        end, price = graph[start][i]

        total_price = current_price + price

        if total_price < price_table[end]:
            price_table[end] = total_price
            heapq.heappush(heap, (total_price, end))

print(price_table[final_end])