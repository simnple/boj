dot = 9
N = int(input())

A = 1
for i in range(2, N+1):
    B = 2**(i-1)
    A += B

    dot += 4*B + B*(2*A-B)

print(dot)