import math

A, B = map(int, input().split())

nums = [True] * (int(math.sqrt(B)) + 1)
nums[0] = nums[1] = False

for i in range(2, int(math.sqrt(math.sqrt(B))) + 1):
    if nums[i]:
        for j in range(i*i, int(math.sqrt(B)) + 1, i):
            nums[j] = False

d = set()
for i in range(2, int(math.sqrt(B)) + 1):
    if nums[i]:
        n = 2
        num = i ** n
        while num <= B:
            if A <= num:
                d.add(num)

            n += 1
            num = i ** n

print(len(d))