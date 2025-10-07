import math

def get_prime_factors(n: int) -> list:
    # _ = 2
    # __ = []

    # while _ <= n:
    #     if n%_ == 0:
    #         __.append(_)
    #         n //= _
        
    #     else:
    #         _ += 1

    # return __

    _ = []
    
    while n % 2 == 0:
        _.append(2)
        n //= 2
    
    __ = 3
    while __**2 <= n:
        while n % __ == 0:
            _.append(__)
            n //= __
        
        __ += 2
    
    if n > 1:
        _.append(n)
    
    return _

def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

under_prime = 0
primes = {}

_ = map(int, input().split(" "))
for i in range(next(_), next(_)+1):
    __ = len(get_prime_factors(i))
    if __ in primes:
        if primes[__] == True:
            under_prime += 1

    else:
        if is_prime(__):
            under_prime += 1
            primes[__] = True
        else:
            primes[__] = False

print(under_prime)
