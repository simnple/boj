import sys

input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))

total = sum(T) + (len(T) - 1) * 8
print(*divmod(total, 24))