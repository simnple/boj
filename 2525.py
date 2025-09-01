A, B = map(int, input().split())
C = int(input())

B += C

if B >= 60:
    A += 1
    B %= 60
    C -= B + 1

A += C // 60
A %= 24

print(A, B)