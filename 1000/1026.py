size = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B = sorted(B, reverse=True)

result = 0

for i in range(size):
    result += A[i] * B[i]

print(result)
