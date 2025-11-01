from itertools import combinations

n = int(input())

primes = []
copy_n = n

for i in range(2, int(n ** 0.5) + 1):
    if copy_n % i == 0:
        primes.append(i)

        while copy_n % i == 0: copy_n //= i

if copy_n > 1:
    primes.append(copy_n)

total = 0

for i in range(1, len(primes) + 1):
    for j in combinations(primes, i):
        temp = 1
        for k in j:
            temp *= k

        total = total + ((-1) ** (i - 1)) * ((n - 1) // temp)

print(n - total - int(n != 1))