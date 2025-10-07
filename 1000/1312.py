A, B, N = map(int, input().split())

remainder = -1
idx = 0

while remainder != 0 and idx <= N:
    quotient = A // B
    remainder = A - quotient * B
    A = remainder * 10
    idx += 1

if idx <= N and remainder == 0: quotient = 0

print(quotient)