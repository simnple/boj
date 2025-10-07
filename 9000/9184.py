memories = [[[0] * 21 for __ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    elif a < b < c:
        return memories[a][b][c-1] + memories[a][b-1][c-1] - memories[a][b-1][c]

    else:
        return memories[a-1][b][c] + memories[a-1][b-1][c] + memories[a-1][b][c-1] - memories[a-1][b-1][c-1]

for i in range(21):
    for j in range(21):
        for k in range(21):
            memories[i][j][k] = w(i, j, k)

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1: break

    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")