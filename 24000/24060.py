def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    i, j, t = p, q + 1, 1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            result.append(A[i])
            tmp[t] = A[i]; t += 1; i += 1
        else:
            result.append(A[j])
            tmp[t] = A[j]; t += 1; j += 1
    while i <= q:
        result.append(A[i])
        tmp[t] = A[i]; t += 1; i += 1
    while j <= r:
        result.append(A[j])
        tmp[t] = A[j]; t += 1; j += 1
    i, t = p, 1
    while i <= r:
        A[i] = tmp[t]; i += 1; t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))

result = []
tmp = [0] * (N + 1)
merge_sort(A, 0, N - 1)

if K - 1 < len(result):
    print(result[K - 1])
else:
    print(-1)