import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(sum(B), sum(A))