import sys

input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

maximum = 0
for y in range(N):
    for x in range(M):
        if x + 3 < M:
            maximum = max(maximum, box[y][x] + box[y][x+1] + box[y][x+2] + box[y][x+3])
        if y + 3 < N:
            maximum = max(maximum, box[y][x] + box[y+1][x] + box[y+2][x] + box[y+3][x])
        if x + 1 < M and y + 1 < N:
            maximum = max(maximum, box[y][x] + box[y][x+1] + box[y+1][x] + box[y+1][x+1])
        if x + 1 < M and y + 2 < N:
            maximum = max(
                maximum, 
                box[y][x] + box[y+1][x] + box[y+2][x] + box[y+2][x+1],
                box[y][x] + box[y+1][x] + box[y+2][x] + box[y][x+1],
                box[y][x] + box[y][x+1] + box[y+1][x+1] + box[y+2][x+1],
                box[y][x] + box[y+1][x] + box[y+2][x] + box[y+1][x+1],
                box[y][x] + box[y+1][x] + box[y+1][x+1] + box[y+2][x+1]
            )
        if x + 2 < M and y + 1 < N:
            maximum = max(
                maximum, 
                box[y][x] + box[y][x+1] + box[y][x+2] + box[y+1][x+2],
                box[y][x] + box[y][x+1] + box[y][x+2] + box[y+1][x],
                box[y][x] + box[y][x+1] + box[y][x+2] + box[y+1][x+1],
                box[y][x] + box[y][x+1] + box[y+1][x+1] + box[y+1][x+2]
            )
        if 0 <= x - 1 and y + 2 < N:
            maximum = max(
                maximum, 
                box[y][x] + box[y+1][x] + box[y+2][x] + box[y+2][x-1],
                box[y][x] + box[y+1][x] + box[y+2][x] + box[y+1][x-1],
                box[y][x] + box[y+1][x] + box[y+1][x-1] + box[y+2][x-1]
            )
        if x + 2 < M and 0 <= y - 1:
            maximum = max(
                maximum,
                box[y][x] + box[y][x+1] + box[y][x+2] + box[y-1][x+2],
                box[y][x] + box[y][x+1] + box[y][x+2] + box[y-1][x],
                box[y][x] + box[y][x+1] + box[y][x+2] + box[y-1][x+1],
                box[y][x] + box[y][x+1] + box[y-1][x+1] + box[y-1][x+2]
            )

print(maximum)