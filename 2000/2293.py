import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])
dp = [0] * (k + 1)

for i in a:
    if i > k: break
    dp[i] += 1
    for j in range(i + 1, k + 1):
        dp[j] += dp[j - i]

print(dp[k])