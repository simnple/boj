import sys

MOD = 1_000_000_007
input = sys.stdin.readline

fibo = [1, 1]

for i in range(2, 191_230):
    fibo.append((fibo[i - 1] + fibo[i - 2]) % MOD)

T = int(input())
for _ in range(T):
    N = int(input())
    print(fibo[N])