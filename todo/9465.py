import sys

input = sys.stdin.readline
directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())

for _ in range(T):
    n = int(input())

    stickers = [list(map(int, input().split())) for _ in range(2)]
    total_stickers = sum([sum(sticker) for sticker in stickers])
    total = 0

    while total_stickers > 0:
        max_value = 0
        max_pos = (-1, -1)
        for y in range(2):
            for x in range(n):
                if max_value < stickers[y][x]:
                    max_value = stickers[y][x]
                    max_pos = (x, y)

        total += max_value
        x, y = max_pos

        for d in directions:
            dx, dy = d
            if (0 <= x + dx <= n - 1) and (0 <= y + dy <= 1):
                total_stickers -= stickers[y + dy][x + dx]
                stickers[y + dy][x + dx] = 0

    print(total)