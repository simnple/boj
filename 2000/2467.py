N = int(input())
nums = sorted(list(map(int, input().split())), key=lambda x: abs(x))

min_values = (None, None)
for i in range(1, N):
    value = nums[i] + nums[i-1]
    if min_values == (None, None) or abs(sum(min_values)) > abs(value):
        min_values = (nums[i-1], nums[i])

print(*sorted(min_values))