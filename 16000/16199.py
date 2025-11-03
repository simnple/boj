Y1, M1, D1 = map(int, input().split())
Y2, M2, D2 = map(int, input().split())

if M2 > M1 or M2 == M1 and D2 >= D1:
    print(Y2 - Y1)
else:
    print(Y2 - Y1 - 1)

print(Y2 - Y1 + 1)
print(Y2 - Y1)