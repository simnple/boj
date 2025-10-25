import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

total_price = 0
idx = 0

while idx < N:
    if not A[idx]:
        idx += 1
        continue

    if idx + 2 < N and A[idx] > 0 and A[idx + 1] > 0 and A[idx + 2] > 0:
        if A[idx + 1] > A[idx + 2]:
            multiply = min(A[idx], A[idx + 1] - A[idx + 2])
            total_price += 5 * multiply
            A[idx] -= multiply
            A[idx + 1] -= multiply
        else:
            multiply = min(A[idx], A[idx + 1], A[idx+2])
            total_price += 7 * multiply
            A[idx] -= multiply
            A[idx + 1] -= multiply
            A[idx + 2] -= multiply

    elif idx + 1 < N and  A[idx] > 0 and A[idx + 1] > 0:
        multiply = min(A[idx], A[idx + 1])
        total_price += 5 * multiply
        A[idx] -= multiply
        A[idx + 1] -= multiply

    else:
        multiply = A[idx]
        total_price += 3 * multiply
        A[idx] -= multiply

print(total_price)