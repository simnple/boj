N = int(input())
times = [input().split() for _ in range(N)]
available_times = [1] * 721

for start, end in times:
    start_time = max(1, int(start[:2]) * 60 + int(start[2:]) - 600 - 9)
    end_time = min(720, int(end[:2]) * 60 + int(end[2:]) - 600 + 10)

    for i in range(start_time, end_time + 1):
        available_times[i] = 0

result = 0
i = 1
while i < 721:
    if available_times[i] == 0:
        i += 1
    else:
        count = 0
        while i < 721 and available_times[i] == 1:
            count += 1
            i += 1
        result = max(result, count)

print(result)