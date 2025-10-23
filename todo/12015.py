N = int(input())
A = list(map(int, input().split()))
nums = [0] * N

for i in range(N):
    count = 1
    result = sorted(range(i), key=lambda x: (-(A[x] < A[i]), -nums[x]))
    print(A)
    print(result)
    print(nums)
    if result:
        count += nums[result[0]]

    # print(a)
    # for j in range(i):
    #     if A[j] < A[i] and nums[j] > count:
    #         count = nums[j]
    # nums[i] = count + 1
    nums[i] = count

print(max(nums))