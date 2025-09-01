import math

while True:
    n = int(input())
    if n == 0: break

    nums = [True for i in range(0, 2*n+1)]
    nums[0] = nums[1] = False

    for i in range(2, int(math.sqrt(2*n)) + 1):
        if nums[i]:
            for j in range(i*i, 2*n+1, i):
                nums[j] = False

    count = 0
    for i in range(n + 1, 2*n+1):
        if nums[i]:
            count += 1

    print(count)