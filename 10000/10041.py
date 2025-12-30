import sys

input = sys.stdin.readline

W, H, N = map(int, input().split())
dist = [tuple(map(int, input().split())) for _ in range(N)]

result = 0
prev_x, prev_y = dist[0]
for i in range(1, N):
    curr_x, curr_y = dist[i]
    diff_x, diff_y = curr_x - prev_x, curr_y - prev_y

    if diff_x > 0 and diff_y > 0:
        value = min(diff_x, diff_y)
        result += value
        prev_x += value
        prev_y += value

        diff_x -= value
        diff_y -= value

    elif diff_x < 0 and diff_y < 0:
        value = min(abs(diff_x), abs(diff_y))
        result += value
        prev_x -= value
        prev_y -= value

        diff_x += value
        diff_y += value

    if diff_x != 0:
        result += abs(diff_x)

    if diff_y != 0:
        result += abs(diff_y)
    
    prev_x, prev_y = curr_x, curr_y

print(result)