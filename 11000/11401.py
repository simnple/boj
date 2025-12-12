MOD = 1_000_000_007

N, K = map(int, input().split())
factorial = [1] * (N + 1)

for i in range(2, N + 1):
    factorial[i] *= (i * factorial[i - 1]) % MOD

print((factorial[N] * pow(factorial[K] * factorial[N - K], MOD - 2, MOD)) % MOD)