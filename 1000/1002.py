T = int(input())

for _ in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())

    distance = (x_2 - x_1) ** 2 + (y_2 - y_1) ** 2

    if x_1 == x_2 and y_1 == y_2 and r_1 == r_2:
        print(-1)
    elif abs(r_1 - r_2) ** 2 < distance < (r_1 + r_2) ** 2:
        print(2)
    elif distance == abs(r_1 - r_2) ** 2 or distance == (r_1 + r_2) ** 2:
        print(1)
    else:
        print(0)