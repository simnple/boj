T = int(input())

for _ in range(T):
    A, B = map(lambda x: int(x, 2), input().split())
    print(bin(A + B)[2:])