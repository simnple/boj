import sys, math

def input(): return sys.stdin.readline().rstrip()

nums = []
_ = [int(input()) for i in range(int(input()))]

for x in _:
    nums = [True for i in range(x+1)]
    nums[0] = nums[1] = False

    for i in range(0, int(math.sqrt(x))+1):
        if nums[i]:
            for j in range(i*i, x+1, i):
                nums[j] = False

    for i in range(x // 2, 1, -1):
        if nums[i] and nums[x-i]:
            print(i, x-i)
            break
