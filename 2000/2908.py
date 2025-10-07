def reverse_int(x):
    return int(x[2] + x[1] + x[0])

A, B = map(reverse_int, input().split())

print(max(A, B))