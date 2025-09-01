# 너무화가난다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def base_10_to_36(x):
    if x == 0: return 0
    result = []
    while x != 0:
        if x % 36 > 9:
            result.append(chr(ord("A") + (x % 36) - 10))
        else:
            result.append(str(x % 36))
        x //= 36
    return "".join(result[::-1])

nums_dict = dict()
nums_count = dict()
nums = []

N = int(input())
for _ in range(N):
    s = input()
    nums.append(s)
    for d in range(len(s)):
        if nums_dict.get(s[d]) == None:
            nums_dict[s[d]] = 10**(len(s)-d)
        else:
            nums_dict[s[d]] += 10**(len(s)-d)
        if nums_count.get(s[d]) == None:
            nums_count[s[d]] = 1
        else:
            nums_count[s[d]] += 1

K = int(input())

words = sorted(nums_dict, key=lambda x: (-len(str(nums_dict[x])), -nums_count[x], -nums_dict[x]))
temp_nums = nums[:]
for i in range(N):
    for j in words[:K]:
        temp_nums[i] = temp_nums[i].replace(j, "Z")
print(words)

words = sorted(nums_dict, key=lambda x: (-len(str(nums_dict[x])), nums_count[x], -nums_dict[x]))
temp_nums_2 = nums[:]
for i in range(N):
    for j in words[:K]:
        temp_nums_2[i] = temp_nums_2[i].replace(j, "Z")
print(words)

print(base_10_to_36(max(sum(map(lambda x: int(x, 36), temp_nums)), sum(map(lambda x: int(x, 36), temp_nums_2)))))