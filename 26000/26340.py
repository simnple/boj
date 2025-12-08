n = int(input())

for i in range(n):
    side_1, side_2, fold = map(int, input().split())

    print(f"Data set: {side_1} {side_2} {fold}")
    for _ in range(fold):
        if side_1 <= side_2:
            side_2 //= 2
        else:
            side_1 //= 2

    print(*sorted([side_1, side_2])[::-1])
    print()