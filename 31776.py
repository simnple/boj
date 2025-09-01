count = 0
for _ in range(int(input())):
    T1, T2, T3 = map(int, input().replace("-1", "999").split())

    if T1 <= T2 <= T3 and min(T1, T2, T3) != 999:
        count += 1

print(count)