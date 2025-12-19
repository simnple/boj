import heapq
import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    max_heap = []
    min_heap = []

    k = int(input())
    visited = [0] * k

    for i in range(k):
        operator, value = input().split()
        value = int(value)

        if operator == "I":
            heapq.heappush(max_heap, (-value, i))
            heapq.heappush(min_heap, (value, i))
            visited[i] = 1

        else:
            if value == 1:
                while max_heap and visited[max_heap[0][1]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    pop_value, idx = heapq.heappop(max_heap)
                    visited[idx] = 0

            else:
                while min_heap and visited[min_heap[0][1]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    pop_value, idx = heapq.heappop(min_heap)
                    visited[idx] = 0

    while max_heap and visited[max_heap[0][1]] == 0:
        heapq.heappop(max_heap)

    while min_heap and visited[min_heap[0][1]] == 0:
        heapq.heappop(min_heap)
    
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    
    else:
        print("EMPTY")