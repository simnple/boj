import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp_inc = [1] * N
dp_dec = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp_inc[i] < dp_inc[j] + 1:
            dp_inc[i] = dp_inc[j] + 1

for i in range(N - 1, -1, -1):
    for j in range(i, N):
        if A[i] > A[j] and dp_dec[i] < dp_dec[j] + 1:
            dp_dec[i] = dp_dec[j] + 1

result = 0
for i in range(N):
    value = dp_inc[i] + dp_dec[i] - 1
    if result < value:
        result = value

print(result)