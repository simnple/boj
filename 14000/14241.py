import heapq

N = int(input())
A = list(map(int, input().split()))

result = 0
while len(A) > 1:
    x = heapq.heappop(A)
    y = heapq.heappop(A)

    heapq.heappush(A, x + y)
    result += x * y

print(result)