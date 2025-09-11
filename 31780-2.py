import math

X, M = map(int, input().split())

total = X

for _ in range(M):
    total += int(X/2)
    total += math.ceil(X/2)

print(total)