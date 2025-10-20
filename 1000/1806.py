N, S = map(int, input().split())
nums = list(map(int, input().split()))
total_nums = [0]

for i in range(1, N + 1):
    total_nums.append(total_nums[i - 1] + nums[i - 1])

min_len = 0
start, end = 0, 0
while end < N + 1:
    value = total_nums[end] - total_nums[start]
    if value < S:
        end += 1
    
    elif value >= S:
        if min_len == 0 or end - start < min_len:
            min_len = end - start
        start += 1

print(min_len)