import sys

input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))

result = 0
for i in range(N):
    j = 0
    k = N - 1
    while j < k:
        if j == i:
            j += 1
            continue
        elif k == i:
            k -= 1
            continue

        if A[j] + A[k] < A[i]:
            j += 1
        elif A[j] + A[k] > A[i]:
            k -= 1
        else:
            result += 1
            break

print(result)