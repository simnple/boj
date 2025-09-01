import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))

for i in range(len(A)):
