MOD = 1_000_000_007

N, R = map(int, input().split())

factorial = [0] * (N + 1)
factorial[0] = 1

for i in range(1, N + 1):
    factorial[i] = (i * factorial[i - 1]) % MOD

print((factorial[N] * pow(factorial[R] * factorial[N - R], MOD - 2, MOD)) % MOD)