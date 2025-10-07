h, w = map(int, input().split())

A = [list(map(int, input().split())) for i in range(h)]
B = [list(map(int, input().split())) for i in range(h)]

C = [[] * 3]

for i in range(h):
    for j in range(w):
        print(A[i][j] + B[i][j], end = " ")
    
    print()
