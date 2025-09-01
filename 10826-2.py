n = int(input())
nums = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1 or i == 2:
        nums[i-1] = 1
    else:
        nums[i-1] = nums[i-2] + nums[i-3]

print(nums[n-1])