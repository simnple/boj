MOD = 1_000_000_007

N, M = map(int, input().split())

factorial = [0] * (N + 1)
factorial[1] = 1

for i in range(2, N + 1):
    factorial[i] = i * factorial[i - 1] % MOD

print(factorial[N] % MOD * pow(factorial[N - M] * factorial[M], MOD - 2, MOD) % MOD)