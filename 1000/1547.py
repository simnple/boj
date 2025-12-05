cups = [1, 0, 0]

M = int(input())

for _ in range(M):
    X, Y = map(lambda x: int(x) - 1, input().split())

    cups[X], cups[Y] = cups[Y], cups[X]

print(cups.index(1) + 1)