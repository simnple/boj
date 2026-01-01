H, W, C = map(int, input().split())
A = [0] + list(map(int, input().split()))

box = [[0] * W for _ in range(H)]

color = 1
x = y = 0
do_right = True
while not y == H:
    while not A[color]:
        color += 1
    
    box[y][x] = str(color)
    A[color] -= 1

    if do_right:
        x += 1
        if x == W:
            do_right = False
            y += 1
            x -= 1

    else:
        x -= 1
        if x == -1:
            do_right = True
            y += 1
            x += 1

print(*["".join(lines) for lines in box], sep="\n")