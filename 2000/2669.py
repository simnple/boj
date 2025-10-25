tables = [[0] * 101 for _ in range(101)]

total = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            if not tables[y][x]:
                tables[y][x] = 1
                total += 1

print(total)