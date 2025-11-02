T = int(input())

print("Gnomes:")
for i in range(T):
    a, b, c = map(int, input().split())

    if a < b < c or c < b < a:
        print("Ordered")
    else:
        print("Unordered")