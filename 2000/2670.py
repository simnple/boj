import sys

input = sys.stdin.readline

N = int(input())
A = [float(input()) for _ in range(N)]

max_value = A[0]
prev_value = A[0]
for i in range(1, N):
    value = max(A[i], prev_value * A[i])
    prev_value = value

    if max_value < value:
        max_value = value

print(f"{max_value:.3f}")