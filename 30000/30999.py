import sys

input = sys.stdin.readline

N, M = map(int, input().split())

count = 0
for _ in range(N):
    count += int(input().count("O") > (M // 2))

print(count)