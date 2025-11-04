n = int(input())

nums = [i for i in range(1, 6)]
nums += nums[3:0:-1]
print(nums[(n - 1) % 8])