P = int(input())

for _ in range(P):
    N, D, A, B, F = map(float, input().split())

    print(int(N), format(D / (A + B) * F, ".6f"))