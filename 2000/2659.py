from collections import deque

def get_nums(i):
    num = deque(list(str(i)))
    nums = set()

    for _ in range(4):
        nums.add(int("".join(num)))
        num.append(num.popleft())
    
    return nums

clock_nums = [1] * (10000)

for i in range(1111):
    clock_nums[i] = 0

for i in range(1111, 10000):
    if "0" in str(i):
        clock_nums[i] = 0
        continue

    nums = get_nums(i)
    nums.remove(min(nums))
    
    for j in nums:
        clock_nums[j] = 0

count = 0
for i in range(min(get_nums("".join(input().split())))):
    if clock_nums[i]:
        count += 1

print(count + 1)