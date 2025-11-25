import sys

input = sys.stdin.readline

X, Y = map(int, input().split())
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    if x != X and y != Y:
        print(1)
    else:
        print(0)