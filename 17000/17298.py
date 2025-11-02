N = int(input())
A = list(map(int, input().split()))

stack = []
result = [-1] * N

for i in range(N - 1, -1, -1):
    while stack and stack[-1] <= A[i]: stack.pop()

    if stack: result[i] = stack[-1]

    stack.append(A[i])

print(*result)