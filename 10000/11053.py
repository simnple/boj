import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    max_len = 0
    for j in range(i):
        if A[j] < A[i] and (max_len == 0 or dp[j] > max_len):
            max_len = dp[j]
    dp[i] = max_len + 1

print(max(dp))