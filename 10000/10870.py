nums = {}

def fibonacci(num):
    if num == 1: return 1
    elif num == 0: return 0
    else:
        if nums.get(num-1) == None: nums[num-1] = fibonacci(num-1)
        if nums.get(num-2) == None: nums[num-2] = fibonacci(num-2)

        return nums[num-1] + nums[num-2]

print(fibonacci(int(input())))