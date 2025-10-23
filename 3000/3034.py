N, W, H = map(int, input().split())
value = (W ** 2 + H ** 2) ** 0.5

for _ in range(N):
    length = int(input())

    if length <= value:
        print("DA")
    else:
        print("NE")