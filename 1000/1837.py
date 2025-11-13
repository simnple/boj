import math

P, K = map(int, input().split())

primes = [1] * (K + 1)
primes[0] = primes[1] = 0

for i in range(2, math.isqrt(K) + 1):
    if primes[i]:
        for j in range(i*i, K + 1, i):
            primes[j] = 0

for i in range(2, K):
    if primes[i] and P % i == 0:
        print("BAD", i)
        break
else:
    print("GOOD")