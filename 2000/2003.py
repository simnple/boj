N, M = map(int, input().split())
A = list(map(int, input().split()))
total_A = [0]

for i in range(1, N + 1):
    total_A.append(total_A[i - 1] + A[i - 1])

count = 0
start = end = 0

while end < N + 1:
    value = total_A[end] - total_A[start]

    if value > M:
        start += 1
    elif value < M:
        end += 1
    else:
        count += 1
        start += 1

print(count)