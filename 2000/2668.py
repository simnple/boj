import sys

input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

results = []
for i in range(N):
    list_in = [0] * N
    list_out = [0] * N

    head = i
    tail = A[head] - 1

    while not list_in[head] or not list_out[tail]:
        list_in[head] = 1
        list_out[tail] = 1

        head = tail
        tail = A[head] - 1

    if list_in == list_out:
        results.append(i + 1)

print(len(results), *results, sep="\n")