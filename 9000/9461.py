# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49

# a(n) = a(n-2) + a(n-3)

import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())
PN = [int(input()) for _ in range(T)]

nums = [1, 1, 1]
for n in PN:
    for i in range(3, n+1):
        if len(nums) == i:
            nums.append(0)
            nums[i] = nums[i-2] + nums[i-3]
    print(nums[n-1])