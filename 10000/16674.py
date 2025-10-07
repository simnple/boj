N = input()

nums = {
    "0": 0,
    "1": 0,
    "2": 0,
    "8": 0,
    "other": 0
}

for s in N:
    if s in nums.keys():
        nums[s] += 1
    else:
        nums["other"] += 1

if nums["other"] > 0:
    print(0)

elif nums["0"] == nums["1"] == nums["2"] == nums["8"] != 0:
    print(8)

elif not nums["0"] or not nums["1"] or not nums["2"] or not nums["8"]:
    print(1)

else:
    print(2)