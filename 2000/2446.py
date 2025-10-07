N = int(input())

for i in range(N-1):
    print(" " * (i) + "*" * (2*N-1-2*i))

print(" " * (N - 1) + "*")

for i in range(N-1):
    print(" " * (N-i-2) + "*" * ((i+1)*2+1))
