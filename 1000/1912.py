import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

prev_num = max_num = A[0]

for i in range(1, N):
    num = max(prev_num + A[i], A[i])
    prev_num = num

    if max_num < num:
        max_num = num

print(max_num)