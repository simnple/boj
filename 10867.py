import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
K = set(map(int, input().split()))

print(*sorted(K))