import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

pws = {}
for _ in range(N):
    site, pw = input().split()
    pws[site] = pw

for _ in range(M):
    print(pws[input()])