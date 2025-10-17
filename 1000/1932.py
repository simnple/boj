import sys

input = sys.stdin.readline

n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    temp_nums = [[] for _ in range(len(nums[i]))]

    for j in range(len(nums[i-1])):
        temp_nums[j].append(nums[i-1][j] + nums[i][j])
        temp_nums[j + 1].append(nums[i-1][j] + nums[i][j + 1])

    for j in range(len(temp_nums)):
        nums[i][j] = max(temp_nums[j])

print(max(nums[-1]))