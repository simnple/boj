import sys

input = sys.stdin.readline

N = int(input())
A = sorted([int(input()) for _ in range(N)], reverse=True)

max_weight = 0
for i in range(N):
    weight = A[i] * (i + 1)
    if weight > max_weight:
        max_weight = weight

print(max_weight)