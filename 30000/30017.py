A, B = map(int, input().split())
print(min(A, B + 1) + min(A - 1, B))