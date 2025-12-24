MOD = 10**9 + 7
N, M = map(int, input().split())

print(pow(3, ((N - 1) * M + (M - 1) * N), MOD))