months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

count = 6
day = month = 1

x, y = map(int, input().split())

while month < x or (month == x and day <= y):
    count = (count + 1) % 7
    day += 1

    if day > months[month]:
        day = 1
        month += 1

print(days[count])