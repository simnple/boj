N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(1, N):
    if A[i-1] >= A[i]:
        A[i] += K
        count += 1

        if A[i-1] >= A[i]:
            count = -1
            break

print(count)