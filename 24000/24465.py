import sys

input = sys.stdin.readline

def birth_to_zodiac(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return 0
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 1
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 2
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 3
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return 4
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return 5
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 6
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 7
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 8
    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        return 9
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return 10
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return 11

zodiac_sign = [0] * 12

for _ in range(7):
    month, day = map(int, input().split())
    zodiac_sign[birth_to_zodiac(month, day)] = 1

N = int(input())

ppl = sorted([tuple(map(int, input().split())) for _ in range(N)])
is_pass = False

for month, day in ppl:
    if not zodiac_sign[birth_to_zodiac(month, day)]:
        print(month, day)
        is_pass = True

if not is_pass: print("ALL FAILED")