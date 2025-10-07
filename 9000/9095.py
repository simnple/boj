T = int(input())
_ = [int(input()) for i in range(T)]

nums = [0] * (max(_) + 1)

for num in _:
    for i in range(1, num + 1):
        if nums[i] != 0:
            continue

        if i == 1 or i == 2 or i == 3:
            nums[i] = 1

        sum_num = nums[i]
        if i > 3:
            sum_num += nums[i - 3]
        if i > 2:
            sum_num += nums[i - 2]
        if i > 1:
            sum_num += nums[i - 1]

        nums[i] = sum_num

    print(nums[num])