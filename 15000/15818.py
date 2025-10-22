N, M = map(int, input().split())
a = list(map(int, input().split()))

total = 1
for n in a:
    total *= n
print(total % M)