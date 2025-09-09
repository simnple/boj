import sys

def input(): return sys.stdin.readline()

N, X, K = map(int, input().split())

for _ in range(K):
    A, B = map(int, input().split())
    if A == X:
        X = B
    
    elif B == X:
        X = A

print(X)