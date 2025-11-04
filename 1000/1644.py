N = int(input())

nums = [True] * (4_000_000 + 1)
nums[0] = nums[1] = False

for i in range(2, int(4_000_000 ** (0.5)) + 1):
    if nums[i]:
        for j in range(i*i, 4_000_000 + 1, i):
            nums[j] = False

divisors = [0]
for i in range(0, 4_000_000 + 1):
    if nums[i]:
        divisors.append(i + divisors[len(divisors) - 1])

count = 0
i = 0
j = 1

while i < j and i < len(divisors) and j < len(divisors):
    if divisors[j] - divisors[i] >= N:
        if divisors[j] - divisors[i] == N:
            count += 1
        i += 1

    else:
        j += 1

print(count)