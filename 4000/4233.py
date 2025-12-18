import sys

input = sys.stdin.readline

while True:
    p, a = map(int, input().split())
    if p == a == 0: break

    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            print("yes" if pow(a, p, p) == a % p else "no")
            break

    else:
        print("no")