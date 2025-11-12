A, B = map(int, input().split())
K, X = map(int, input().split())

value = len(set(range(A, B + 1)) & set(range(K-X, K+X+1)))

if value == 0:
    print("IMPOSSIBLE")
else:
    print(value)