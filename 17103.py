T = int(input())

maximum = 1_000_000

nums = [True] * (maximum + 1)
nums[0] = nums[1] = False

for i in range(2, int(maximum**(1/2))+1):
    if nums[i]:
        for j in range(i*i, maximum+1, i):
            nums[j] = False

for _ in range(T):
    N = int(input())

    goldbach = 0
    for i in range(2, N // 2 + 1):
        if nums[i] and nums[N-i]:
            goldbach += 1

    print(goldbach)