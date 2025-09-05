N = 318137

nums = [True] * (N + 1)
nums[0] = nums[1] = False
results = []

for i in range(2, int(N ** (1/2)) + 1):
    if nums[i]:
        for j in range(i*i, N + 1, i):
            nums[j] = False

prime_number = 1
for i in range(N + 1):
    if nums[i]:
        if nums[prime_number]:
            results.append(i)
        prime_number += 1

T = int(input())
for _ in range(T):
    n = int(input())
    print(results[n-1])
