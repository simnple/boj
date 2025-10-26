import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    width = int(N ** 0.5)
    height = N // width + (N % width > 0)
    print((width + height) * 2)