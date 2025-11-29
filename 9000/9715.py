import sys

input = sys.stdin.readline

T = int(input())

diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(T):
    R, C = map(int, input().split())
    box = [list(map(int, input().rstrip())) for _ in range(R)]
    
    result = 0
    for y in range(R):
        for x in range(C):
            if box[y][x]:
                # 윗면 + 아랫면
                result += 2

                for dx, dy in diffs:
                    nx, ny = x + dx, y + dy

                    # top에서 본 기준으로 동서남북에 위치한 모형과 비교 (옆면)
                    if not (0 <= nx < C and 0 <= ny < R):
                        result += box[y][x]
                    elif box[ny][nx] < box[y][x]:
                        result += box[y][x] - box[ny][nx]

    print(result)