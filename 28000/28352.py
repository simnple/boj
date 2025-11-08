N = int(input())

result = 1
for i in range(1, N + 1):
    result *= i

print(result // (60 * 60 * 24) // 7)