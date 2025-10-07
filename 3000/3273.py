import sys

def input(): return sys.stdin.readline().rstrip()

n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

dummy_nums = dict()
count = 0
for i in nums:
    start = 0
    end = len(nums) - 1
    if i + i == x: continue
    if i in dummy_nums or x-i in dummy_nums: continue
    while start <= end:
        mid = (end + start) // 2

        if nums[mid] > x-i:
            end = mid - 1
        elif nums[mid] < x-i:
            start = mid + 1
        else:
            dummy_nums[i] = True
            dummy_nums[x-i] = True
            count += 1
            break

print(count)