import sys

def custom_round(num: float) -> int:
    if abs(num) - abs(int(num)) >= 0.5:
        if num < 0:
            return int(num) - 1
        return int(num) + 1
    return int(num)

def get_mode(data: list) -> int:
    nums = dict()

    for num in data:
        if nums.get(num) == None:
            nums[num] = 1
        
        else:
            nums[num] += 1
    
    maximum = max(nums.values())    
    maximum_list = []

    for key in nums:
        if len(maximum_list) > 1:
            break

        if nums[key] == maximum:
            maximum_list.append(key)

    if len(maximum_list) == 2:
        return maximum_list[1]
    
    return maximum_list[0]

_ = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]

_.sort()

print(custom_round(sum(_) / len(_)))
print(_[(len(_)//2)])
print(get_mode(_))
print(_[-1] - _[0])