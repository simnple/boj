N = int(input())

students = list(map(int, input().split()))
stack = []

number = 1
for i in students:
    if i == number:
        number += 1

    else:
        stack.append(i)

    while stack and stack[-1] == number:
        stack.pop()
        number += 1

if stack:
    print("Sad")
else:
    print("Nice")