N = int(input())
price = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = price[0]

for i in range(2, N + 1):
    minimum_value = price[i - 1]

    for j in range(1, i + 1):
        minimum_value = min(minimum_value, dp[i - j] + price[j - 1])

    dp[i] = minimum_value

print(dp[N])