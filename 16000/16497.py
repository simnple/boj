N = int(input())

dates = [0] * 32

for _ in range(N):
    start, end = map(int, input().split())
    dates[start] += 1
    dates[end] -= 1

for i in range(1, 32):
    dates[i] = dates[i] + dates[i - 1]

K = int(input())

print(int(not any(i for i in dates if i > K)))