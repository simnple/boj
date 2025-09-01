X = int(input())

nums = [0] * X
for i in range(1, X + 1):
    count = 0
    if i == 1:
        nums[i-1] = count
    
    else:
        data = []
        if i % 3 == 0:
            data.append(nums[i//3 - 1])
        if i % 2 == 0:
            data.append(nums[i//2 - 1])
        data.append(nums[i-1 - 1])
        
        nums[i-1] = min(data) + 1

print(nums[X-1])