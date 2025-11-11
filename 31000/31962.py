import sys

input = sys.stdin.readline

N, X = map(int, input().split())

value = -1
result = 0
for _ in range(N):
    S, T = map(int, input().split())
    if value < S and S + T <= X:
        value = S
        result = S + T

print(value)