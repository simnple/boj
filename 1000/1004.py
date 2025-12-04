T = int(input())

for _ in range(T):
    circle = 0

    x_1, y_1, x_2, y_2 = map(int, input().split())
    n = int(input())

    for _ in range(n):
        c_x, c_y, r = map(int, input().split())

        d_1 = (x_1 - c_x) ** 2 + (y_1 - c_y) ** 2
        d_2 = (x_2 - c_x) ** 2 + (y_2 - c_y) ** 2

        if (d_1 < r ** 2 and d_2 >= r ** 2) or (d_2 < r ** 2 and d_1 >= r ** 2):
            circle += 1

    print(circle)