import sys

input = sys.stdin.readline

N, M = map(int, input().split())
friends = [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    friends[A - 1] += 1
    friends[B - 1] += 1

print(*friends, sep="\n")