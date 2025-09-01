import math

N = int(input())

nums = [True] * (N + 1)
nums[0] = nums[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if nums[i]:
        for j in range(i*i, N+1, i):
            nums[j] = False

for i in range(N, 1, -1):
    if nums[i]:
        for j in range(N+1):
            if i + j >= N: break
            if nums[j]:
                for k in range(N+1):
                    if i + j + k >= N: break
                    if nums[k]:
                        for l in range(N+1):
                            if nums[l]:
                                if i + j + k + l == N:
                                    print(i, j, k, l)
                                    exit()

print(-1)