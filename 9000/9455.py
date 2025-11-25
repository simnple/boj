import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(m)]

    move_count = 0
    for x in range(n):
        last_filled_box = 0
        for y in range(m - 1, -1, -1):
            if box[y][x] == 1:
                move_count += m - 1 - last_filled_box - y
                last_filled_box += 1

    print(move_count)