N = int(input())

minimum = -1
for _ in range(N):
    A, B = map(int, input().split())
    if A <= B and (minimum == -1 or minimum > B):
        minimum = B

print(minimum)