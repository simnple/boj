K = int(input())
N = 10_000_000 # K개 넘게 들어있음.

nums = [True] * (N + 1)
nums[0] = nums[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if nums[i]:
        for j in range(i * i, N + 1, i):
            nums[j] = False

count = 1
for i in range(N + 1):
    if nums[i]:
        if count == K:
            print(i)
            break

        count += 1