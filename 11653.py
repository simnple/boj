def get_prime_factorization(x):
    primes = []
    num = 2
    while x > 1:
        if x % num == 0:
            x //= num
            primes.append(num)
        else:
            num += 1
    return primes

N = int(input())
if N > 1:
    print(*get_prime_factorization(N), sep="\n")