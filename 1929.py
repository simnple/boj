import sys, math

def input(): return sys.stdin.readline().rstrip()

M, N = map(int, input().split())

nums = [True for i in range(0, N + 1)]
nums[0] = nums[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if nums[i]:
        for j in range(i * i, N + 1, i):
            nums[j] = False

for i in range(M, N + 1):
    if nums[i] == True:
        print(i)