MOD = 1_000_000_000

N = int(input())

# 0 1 1 1 1 1 1 1 1 1
dp = [1] * 10
dp[0] = 0

for i in range(1, N):
    temp = [0] * 10

    for j in range(10):
        if j == 0:
            temp[1] += dp[j] % MOD
        elif j == 9:
            temp[8] += dp[j] % MOD
        else:
            temp[j - 1] += dp[j] % MOD
            temp[j + 1] += dp[j] % MOD
    dp = temp.copy()

print(sum(dp) % MOD)