import sys

input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
M = int(input())
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][i] = 1

for i in range(1, N):
    if A[i] == A[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, N + 1):
    for j in range(1, N - i + 1):
        dp[j][j+i] = int(A[j] == A[j+i] and dp[j+1][j+i-1])

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])