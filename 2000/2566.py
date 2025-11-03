nums = [list(map(int, input().split())) for _ in range(9)]

pos = (0, 0)

for y in range(9):
    for x in range(9):
        if nums[y][x] > nums[pos[0]][pos[1]]:
            pos = [y, x]

print(nums[pos[0]][pos[1]])
print(*[i + 1 for i in pos])