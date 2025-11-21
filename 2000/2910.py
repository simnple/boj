import sys

input = sys.stdin.readline

N, C = map(int, input().split())
A = list(map(int, input().split()))

counter = dict()
for i in range(N):
    if counter.get(A[i]):
        counter[A[i]] += 1
    else:
        counter[A[i]] = 1

result = []
for key, value in sorted(counter.items(), key=lambda x: -x[1]):
    for _ in range(value):
        result.append(key)

print(*result)