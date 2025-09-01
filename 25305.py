import sys

def input(): return sys.stdin.readline().rstrip()

N, k = map(int, input().split())
x = sorted(list(map(int, input().split())), reverse=True)
print(x[k-1])