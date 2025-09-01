import sys
input = sys.stdin.readline

N = int(input())

schedule = []
for _ in range(N):
    start, end = map(int, input().split())
    schedule.append((end, start))
schedule = sorted(schedule, reverse=True, key=lambda x: (x[1], x[0]))

ans, last_start = 0, -1
for end, start in schedule:
    if last_start == -1 or last_start >= end:
        # print(start, end)
        last_start = start
        ans += 1

print(ans)