from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
queue = deque([B[i] for i in range(N) if A[i] == 0])

M = int(input())
C = list(map(int, input().split()))

results = []
for i in range(M):
    queue.appendleft(C[i])
    results.append(queue.pop())

print(*results)