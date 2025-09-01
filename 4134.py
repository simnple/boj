import math
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    if n < 2:
        n = 2

    if n % 2 == 0 and n > 2:
        n += 1

    while True:
        is_prime = True
        for j in range(2, int(math.sqrt(n)) + 1):
            if n % j == 0:
                is_prime = False
                break

        if is_prime == True:
            print(n)
            break

        n += 2