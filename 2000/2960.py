import sys, math

def input(): return sys.stdin.readline().rstrip()

N, K = map(int, input().split())

nums = [True for i in range(N+1)]
nums[0] = nums[1] = False

count = 0
for i in range(2, N + 1):
    if nums[i]:
        nums[i] = False
        count += 1
        if count == K:
            print(i)
            exit()

        for j in range(i*i, N+1, i):
            if nums[j]:
                nums[j] = False
                count += 1
                if count == K:
                    print(j)
                    exit()
