nums = {0: 0, 1: 1}

def fibonacci(x):
    if x == 0: return 0
    elif x == 1: return 1
    else:
        if not nums.get(x-1):
            nums[x-1] = fibonacci(x-1)

        elif not nums.get(x-2):
            nums[x-2] = fibonacci(x-2)

        return nums[x-1] + nums[x-2]

n = int(input())

print(fibonacci(n))