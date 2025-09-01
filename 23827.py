import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))

total = 0
for i in range(len(A)):
    for j in range(i+1, len(A)):
        total += A[i] * A[j] % 1_000_000_007

print(total % 1_000_000_007)