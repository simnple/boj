X, Y = map(int, input().split())
Z = Y * 100 // X

if Z >= 99:
    print(-1)
    exit()

high = 1000000000
low = 1

result = -1

while low <= high:
    mid = (high + low) // 2
    num = (Y + mid) * 100 // (X + mid)

    if num > Z:
        result = mid
        high = mid - 1

    else:
        low = mid + 1

print(result)