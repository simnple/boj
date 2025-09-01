N = 20000000000002

print(int((N ** (1/2)) + 1), int(N ** (1/4) + 1))

nums = [True] * int(N ** (1/2) + 1)
nums[0] = nums[1] = False

for i in range(int(N ** (1/2) + 1)):
    if nums[i]:
        for j in range(i*i, int(N ** (1/4) + 1), i):
            nums[j] = False

result = "NO"
for i in range(1_000_000, int(N ** (1/2) + 1)):
    if nums[i] and nums[N // i] and N % i == 0:
        result = "YES"
        break

print(result)