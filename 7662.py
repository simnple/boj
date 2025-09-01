import heapq
import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    k = int(input())
    heap = []

    for __ in range(k):
        cmd, num = input().split()
        num = int(num)

        if cmd == "I":
            heapq.heappush(heap, num)

        elif cmd =="D" and heap:
            if num == 1:
                heap.pop()

            else:
                heapq.heappop(heap)

    if len(heap):
        print(heap)
        print(heap[-1], heap[0])

    else:
        print("EMPTY")