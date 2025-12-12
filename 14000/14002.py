N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
history = [-1] * N

largest_idx = 0
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1
            history[i] = j

            if dp[largest_idx] < dp[i]:
                largest_idx = i

print(dp[largest_idx])

result = []
while largest_idx > -1:
    result.append(A[largest_idx])
    largest_idx = history[largest_idx]

print(*result[::-1])