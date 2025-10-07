N, S = map(int, input().split())
_ = list(map(int, input().split()))

nums = [_[0]]
for i in range(1, len(_)):
    nums.append(_[i] + nums[i-1])

size = 1
result = 0

# print(nums)

while size <= N:
    for i in range(0, N):
        start = i
        end = start + size
        if end >= N: break

        # print(nums[end], nums[start], size)

        if nums[end] - nums[start] >= S:
            # print("this!", nums[end], nums[start])
            result = size
            size = N + 1
            break
    size += 1

if nums[-1] >= S:
    result = N

print(result)