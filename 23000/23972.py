K, N = map(int, input().split())
if N > 1:
    print(K * N // (N-1) + (K * N % (N-1) != 0))
else:
    print(-1)