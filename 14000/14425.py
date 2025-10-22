import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

s = set()
for _ in range(N):
    s.add(input())

count = 0
for _ in range(M):
    if s & set([input()]):
        count += 1

print(count)