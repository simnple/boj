n = list(map(int, input().split()))

while n != [1, 2, 3, 4, 5]:
    if n[0] > n[1]:
        n[0], n[1] = n[1], n[0]
        print(*n)
    if n[1] > n[2]:
        n[1], n[2] = n[2], n[1]
        print(*n)
    if n[2] > n[3]:
        n[2], n[3] = n[3], n[2]
        print(*n)
    if n[3] > n[4]:
        n[3], n[4] = n[4], n[3]
        print(*n)