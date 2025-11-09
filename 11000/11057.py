MOD = 10_007

N = int(input())

dp = [[1] * 10 for _ in range(N + 1)]
for i in range(2, N + 1):
    for j in range(8, -1, -1):
        dp[i][j] = (dp[i][j+1] + dp[i-1][j]) % MOD

print(sum(dp[N]) % MOD)