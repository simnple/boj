import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    if N == 0:
        print()
    elif N == 1:
        print("#")
    else:
        print("#" * N)
        for i in range(N-2):
            print("#" + "J" * (N-2) + "#")
        print("#" * N)
    print()