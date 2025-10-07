for _ in range(int(input())):
    __ = map(int, input().split(" "))
    if next(__) + next(__) == 1:
        print(0)
    else:
        print(1)