N = int(input())
CHICKEN = list(map(int, input().split()))
k = int(input())

while N > 1:
    if N == k:
        break

    N //= 2

    temp = []
    for j in range(0, len(CHICKEN), len(CHICKEN) // N):
        temp.extend(sorted(CHICKEN[j:j+(len(CHICKEN) // N)]))
    CHICKEN = temp

print(*CHICKEN)