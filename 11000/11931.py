import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
_ = [int(input()) for i in range(N)]
for i in sorted(_, reverse=True):
    print(i)