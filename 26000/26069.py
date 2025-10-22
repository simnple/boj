import sys

def input(): return sys.stdin.readline().rstrip()

dancer = set(["ChongChong"])
N = int(input())
for _ in range(N):
    A, B = input().split()
    if A in dancer or B in dancer:
        dancer.add(A)
        dancer.add(B)

print(len(dancer))