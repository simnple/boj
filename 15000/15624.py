MOD = 1_000_000_007

n = int(input())
fib = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1 or i == 2: fib[i] = 1
    else: fib[i] = (fib[i - 1] + fib[i - 2]) % MOD

print(fib[n])