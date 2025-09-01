import sys, math

minimum, maximum = map(int, sys.stdin.readline().split())

nums = [True for i in range(maximum - minimum + 1)]

for i in range(2, int(math.sqrt(maximum)) + 1):
    for j in range((minimum + i*i - 1) // (i*i) * (i*i), maximum + 1, i*i):
        nums[j-minimum] = False

print(sum(nums))