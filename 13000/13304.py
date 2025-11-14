import sys

input = sys.stdin.readline

N, K = map(int, input().split())

students = [0, [0, 0], [0, 0]]

for _ in range(N):
    S, Y = map(int, input().split())

    if Y < 3:
        students[0] += 1
    elif Y < 5:
        students[1][S] += 1
    else:
        students[2][S] += 1

rooms = 0
rooms += students[0] // K + int(students[0] % K > 0)
rooms += students[1][0] // K + int(students[1][0] % K > 0)
rooms += students[1][1] // K + int(students[1][1] % K > 0)
rooms += students[2][0] // K + int(students[2][0] % K > 0)
rooms += students[2][1] // K + int(students[2][1] % K > 0)

print(rooms)