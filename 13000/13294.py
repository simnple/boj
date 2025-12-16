MOD = 1_000_000_007

n = int(input()) % MOD

factorial = i = 1
while True:
    factorial = factorial * i % MOD

    if factorial == n:
        print(i)
        break
    i += 1