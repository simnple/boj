import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
sum_nums = [0]

for i in range(1, N+1):
    sum_nums.append(sum_nums[i-1] + nums[i])

for i in range(M):
    start, end = map(int, input().split())
    print(sum_nums[end] - sum_nums[start-1])