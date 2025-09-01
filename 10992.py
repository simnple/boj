N = int(input())

for i in range(N):
    print(" " * (N-i-1) + "*" + (" " if i < N-1 else "*") * ((i-1)*2 + 1) + "*" * (1 if i > 0 else 0))