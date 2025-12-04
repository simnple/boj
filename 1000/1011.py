T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x

    result = 0
    count = 0
    k = 1
    while result < distance:
        result += k
        count += 1

        if result >= distance:
            break

        result += k
        count += 1
        k += 1

    print(count)