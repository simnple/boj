a, b = map(int, input().split())

result = 1

for i in range(a, b+1):
    temp = 0
    for j in range(1, i+1):
        temp += j
    result *= temp

print(result % 14579)