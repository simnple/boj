N, C = map(int, input().split())
box = [N, N]

for _ in range(C):
    X, Y = map(int, input().split())

    if box[1] <= X or box[0] <= Y: continue

    A = Y * box[1]
    B = X * box[0]
    
    if A > B:
        box[0] = Y
    else:
        box[1] = X

print(box[0] * box[1])