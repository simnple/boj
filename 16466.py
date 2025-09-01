import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
nums = list(range(1, 1_000_001))
result = 0
for i, n in enumerate(sorted(map(int, input().split()))):
    if nums[i] != n:
        result = nums[i]
        break

if result == 0:
    print(nums[i+1])
else:
    print(result)