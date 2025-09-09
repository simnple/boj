L, A, B, C, D = [int(input()) for _ in range(5)]

korean = 0
math = 0

while korean < A or math < B:
    korean += C
    math += D
    L -= 1

print(L)