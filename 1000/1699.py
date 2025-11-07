N = int(input())

dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    if int(i ** (0.5)) ** 2 == i:
        dp[i] = 1

    else:
        for j in range(1, int(i ** (0.5)) + 1):
            if dp[i] == 0: dp[i] = dp[j ** 2] + dp[i - j ** 2]

            else:
                dp[i] = min(dp[i], dp[j ** 2] + dp[i - j ** 2])

print(dp[N])