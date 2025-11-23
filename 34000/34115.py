import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

start_idx = [-1] * (N + 1)
end_idx = [-1] * (N + 1)

for i in range(2 * N):
    if start_idx[X[i]] == -1:
        start_idx[X[i]] = i
    else:
        end_idx[X[i]] = i

K = max(map(lambda x: x[1] - x[0] - 1, zip(start_idx, end_idx)))

print(K)