import sys

input = sys.stdin.readline

N = int(input())
P = sorted(list(map(int, input().split())))

total_time = 0
result = 0

for cur_time in P:
    total_time += cur_time
    result += total_time

print(result)