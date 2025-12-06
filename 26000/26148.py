N = int(input())
day = int(input()) - 1

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 0

for i in range(12):
    months = [0] * 7

    current_days = days[i]
    if i == 1 and ((N % 4 == 0 and N % 100 != 0) or (N % 400 == 0)):
        current_days += 1

    for j in range(current_days):
        months[day] += 1
        day = (day + 1) % 7

    for j in months:
        if j == 5:
            result += 1

print(result)