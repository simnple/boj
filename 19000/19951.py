import sys

input = sys.stdin.readline

N, M = map(int, input().split())
H = [0] + list(map(int, input().split()))
A = [0] * (N + 1)

for _ in range(M):
    start, end, depth = map(int, input().split())
    A[start] += depth
    if end + 1 < N + 1:
        A[end + 1] -= depth

for i in range(1, N + 1):
    A[i] = A[i] + A[i - 1]
    H[i] = H[i] + A[i]

print(*H[1:])