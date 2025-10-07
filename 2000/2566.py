nums = [list(map(int, input().split())) for _ in range(9)]

result = [-1, 0, 0]

for y in range(9):
    for x in range(9):
        if nums[y][x] > result[0]:
            result = [nums[y][x], y+1, x+1]

print(result[0])
print(*result[1:])