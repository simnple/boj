import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

total = 0
for _ in range(N):
    C, K = map(int, input().split())
    total += (((C * (K % 1000000007)) % 1000000007) % 1000000007 * pow(2, K-1, 1000000007)) % 1000000007

print(total % 1000000007)