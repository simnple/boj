nums = [0] * 9

def cround(x):
    if x - int(x) == 0.5: return int(x) + 1
    else: return x

N = input()

for i in N:
    i = int(i)
    if i == 6 or i == 9:
        nums[6] += 0.5
    else:
        nums[i] += 1

nums[6] = int(cround(nums[6]))
print(max(nums))