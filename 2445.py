N = int(input())

for i in range(N-1):
    print("*" * (i+1) + " " * (2*N-2*(i+1)) + "*" * (i+1))

print("*" * (N * 2))

for i in range(N-1):
    print("*" * (N-i-1) + " " * ((i+1)*2) + "*" * (N-i-1))
