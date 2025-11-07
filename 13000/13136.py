R, C, N = map(int, input().split())

print((R // N + int(R % N != 0)) * (C // N + int(C % N != 0)))