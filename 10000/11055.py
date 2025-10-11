import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    max_value = 0
    for j in range(i):
        if A[j] < A[i] and max_value < dp[j]:
            max_value = dp[j]
    dp[i] = A[i] + max_value

print(max(dp))