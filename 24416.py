N = int(input())

fibonacci = [0, 1, 1]

for i in range(3, N + 1):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci[N], N-2)