n = int(input())

count = 0
for i in range(3, n, 3):
    for j in range(3, n, 3):
        if (n - (i + j)) % 3 == 0 and (n - (i + j)) > 2:
            count += 1

print(count)