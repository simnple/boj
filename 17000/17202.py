A = list(map(int, input()))
B = list(map(int, input()))

numbers = []

for i in range(16):
    if i % 2 == 0:
        numbers.append(A[i // 2])
    else:
        numbers.append(B[(i - 1) // 2])

for i in range(16, 2, -1):
    temp = []
    for j in range(i - 1):
        temp.append((numbers[j] + numbers[j + 1]) % 10)
    numbers = temp.copy()

print(f"{numbers[0]}{numbers[1]}")