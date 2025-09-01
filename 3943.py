import sys

def input(): return sys.stdin.readline().rstrip()

def hailstone(n, maximum):
    if n > maximum: maximum = n
    if n == 4 or n == 2 or n == 1:
        return maximum

    if n % 2 == 0:
        return hailstone(n//2, maximum)
    
    else:
        return hailstone(n*3+1, maximum)

T = int(input())

for _ in range(T):
    print(hailstone(int(input()), 0))