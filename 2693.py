import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    A = sorted(list(map(int, input().split())))
    print(A[-3])