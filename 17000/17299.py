import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
F = dict()

for i in range(N):
    if F.get(A[i]):
        F[A[i]] += 1
    else:
        F[A[i]] = 1

R = []
result = []
for i in range(N - 1, -1, -1):
    while R and F[R[-1]] <= F[A[i]]:
        R.pop()
    
    if R: result.append(R[-1])
    else: result.append(-1)

    R.append(A[i])

print(*result[::-1])