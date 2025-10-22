import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

result = 0
for _ in range(N):
    A, B = map(int, input().split())
    result += A - B
    print(result)