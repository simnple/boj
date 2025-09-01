N = int(input())

nums = {i: 0 for i in range(0, 10)}

for i in range(1, N+1):
    for s in str(i):
        nums[int(s)] += 1

print(nums)