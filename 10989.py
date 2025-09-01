import sys

def input(): return sys.stdin.readline().rstrip()

nums = dict()

for _ in range(int(input())):
    num = int(input())
    if nums.get(num) == None:
        nums[num] = 1
    else:
        nums[num] += 1

for _ in sorted(nums):
    for i in range(nums[_]):
        print(_)