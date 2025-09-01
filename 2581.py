import sys, math

def input(): return sys.stdin.readline().rstrip()

M, N = [int(input()) for i in range(2)]

nums = [True for i in range(0, N+1)]
nums[0] = nums[1] = False

for i in range(2, int(math.sqrt(N+1)) + 1):
    if nums[i]:
        for j in range(i * i, N + 1, i):
            nums[j] = False

total = 0
minimum = 0
for i in range(M, N+1):
    if nums[i] == True:
        if minimum == 0: minimum = i
        total += i

if total == 0: print(-1)
else:
    print(total)
    print(minimum)