# 1 2
# 0 0 -> exit

while True:
    _ = list(map(int, input().split(" ")))

    if _ == [0, 0]:
        break

    if _[0] > _[1]:
        print("Yes")
        continue

    print("No")