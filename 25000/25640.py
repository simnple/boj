import sys

input = sys.stdin.readline

JINHO = input()
N = int(input())
count = 0

for _ in range(N):
    if JINHO == input():
        count += 1

print(count)