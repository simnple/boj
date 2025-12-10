import sys

input = sys.stdin.readline

MOD = 1_000_000_007

factorial = [0] * (4_000_000 + 1)
factorial[0] = 1

for i in range(1, 4_000_000 + 1):
    factorial[i] = (i * factorial[i - 1]) % 1_000_000_007

M = int(input())

for _ in range(M):
    N, K = map(int, input().split())

    print((factorial[N] * pow(factorial[K] * factorial[N - K], MOD - 2, MOD)) % MOD)