n, m = map(int, input().split())

result = 1
for i in range(1, n + 1):
    result *= i

a = 1
for i in range(1, n - m + 1):
    a *= i

for i in range(1, m + 1):
    a *= i

print(result // a)