N, K = map(int, input().split())

dp = [0] * (1000 + 1)
dp[0] = 1

for i in range(1, 1000 + 1):
    dp[i] = i * dp[i - 1]

print((dp[N] // (dp[K] * dp[N-K])) % 10007)