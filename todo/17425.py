# A B
# F(A) = A의 약수 합
# x >= y의 모든

import sys

input = sys.stdin.readline

sum_of_divisors = [0] * (1_000_000 + 1)

for n in range(1, 1_000_000 + 1):
    total_divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            total_divisors += i

            if i * i != n:
                total_divisors += n // i
    sum_of_divisors[n] = total_divisors

T = int(input())

for _ in range(T):
    N = int(input())

    print(sum_of_divisors[N])