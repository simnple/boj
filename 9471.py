nums = {0: 0, 1: 1}

def fibonacci(x):
    global temp, period
    if x == 0: return 0
    elif x == 1: return 1
    else:
        if not nums.get(x-1):
            nums[x-1] = fibonacci(x-1) % n

        elif not nums.get(x-2):
            nums[x-2] = fibonacci(x-2) % n
        
        if nums[x-1] == 1 and nums[x-2] == 0:
            if temp == 0: temp = x
            elif period == 0: period = x - temp

        return nums[x-1] + nums[x-2]

for i in range(int(input())):
    temp = 0
    period = 0
    nums = {0: 0, 1: 1}
    k, n = map(int, input().split())
    fibonacci(100)

    print(k, period)