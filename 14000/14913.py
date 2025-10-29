a, d, k = map(int, input().split())

if (k - a) % d != 0 or (k - a) // d < 0:
    print("X")
else:
    print((k - a) // d + 1)