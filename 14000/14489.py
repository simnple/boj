A, B = map(int, input().split())
C = int(input())

value = A + B - C * 2
if value >= 0:
    print(value)
else:
    print(A + B)