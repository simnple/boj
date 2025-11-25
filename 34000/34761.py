import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B[:N] and set(A) == set(B):
    print("YES")
else:
    print("NO")