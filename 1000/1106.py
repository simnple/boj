import sys

input = sys.stdin.readline
INF = float("inf")

C, N = map(int, input().split())
cities = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])

dp = [INF] * (1100 + 1)
minimum_result = INF

for i in range(1, 1100 + 1):
    for j in range(1, i // 2 + 1):
        if dp[j] == INF: continue
        elif dp[i - j] == INF: continue
        dp[i] = min(dp[i], dp[j] + dp[i - j])

    for j in range(N):
        if cities[j][1] == i:
            dp[i] = min(dp[i], cities[j][0])
        elif i - cities[j][1] > 0 and dp[i - cities[j][1]] != INF:
            dp[i] = min(dp[i], cities[j][0] + dp[i - cities[j][1]])
        elif i < cities[j][1]:
            break

    if C <= i:
        minimum_result = min(minimum_result, dp[i])

print(minimum_result)