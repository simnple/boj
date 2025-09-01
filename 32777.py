import sys

input = sys.stdin.readline

Q = int(input())

for _ in range(Q):
    a, b = map(int, input().split())

    inner = 0
    temp_number = a
    while temp_number != b:
        temp_number += 1
        inner += 1
        if temp_number == 244:
            temp_number = 201

    outer = 0
    temp_number = a
    while temp_number != b:
        temp_number -= 1
        outer += 1
        if temp_number == 200:
            temp_number = 243

    if inner < outer:
        print("Inner circle line")
    elif inner > outer:
        print("Outer circle line")
    else:
        print("Same")