import sys

def input(): return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
A = [int(input()) for i in range(N)]

count = 0
for i in range(-1, -len(A) - 1, -1):
    if K == 0: break
    if K // A[i] > 0:
        count += K // A[i]
        K -= (K // A[i]) * A[i]

print(count)