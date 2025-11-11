import sys

input = sys.stdin.readline

price = 1_000_000 * 1_000 * 2

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N - 1):
    price = min(price, X * (A[i] + A[i + 1]))

print(price)