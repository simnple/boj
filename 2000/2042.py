N, M, K = map(int, input().split())

nums = [0] * N

for i in range(N):
    n = int(input())
    if i == 0: nums[i] = n
    else: nums[i] = n + nums[i-1]

change_nums = {}

for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1: change_nums[b-1] = c

    else:
        if b == 1: result = nums[c-1]
        else: result = nums[c-1] - nums[b-2]

        for i in change_nums:
            if b-2 < i <= c-1:
                if i == 0: diff = change_nums[0] - nums[0]
                else: diff = change_nums[i] - (nums[i] - nums[i-1])

                result = result + diff

        print(result)
