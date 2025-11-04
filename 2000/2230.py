import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = sorted([int(input()) for _ in range(N)])

min_diff = 2_000_000_000

i = 0
j = 1

while i < N and j < N:
    diff = A[j] - A[i]

    if diff >= M:
        i += 1
        min_diff = min(min_diff, diff)

    else:
        j += 1

print(min_diff)