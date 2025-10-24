import sys

input = sys.stdin.readline

n = int(input())
grape_juice = [int(input()) for _ in range(n)]

dp = [0] * n

for i in range(n):
    if i < 1:
        dp[i] = grape_juice[i]

    elif i < 2:
        dp[i] = grape_juice[i] + grape_juice[i - 1]

    else:
        dp[i] = max(
            grape_juice[i] + grape_juice[i - 1] + dp[i - 3],
            grape_juice[i] + dp[i - 2],
            dp[i - 1]
        )

print(max(dp))