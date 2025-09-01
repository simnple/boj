import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
nums = sorted([int(input()) for _ in range(N)])

for i in nums:
    print(i)