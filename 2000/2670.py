import sys

input = sys.stdin.readline

N = int(input())
A = [float(input()) for _ in range(N)]

max_value = 0
for i in range(N):
    if A[i] == 0: continue
    value = 1

    for j in range(i, N):
        if A[j] == 0: break
        value *= A[j]
        if max_value < value:
            max_value = value

print(f"{max_value:.3f}")