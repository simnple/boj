import heapq
import sys

def input(): return sys.stdin.readline().rstrip()

heap = []

N = int(input())

for _ in range(N):
    x = int(input())

    if x == 0:
        if heap:
            temp = heapq.heappop(heap)
            print(temp[0] * (-1) ** (temp[1]+1))
        else:
            print(0)

    else:
        heapq.heappush(heap, (abs(x), int(x > 0)))