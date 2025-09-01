import sys

input = sys.stdin.readline

X, K = map(int, input().split())
A = list(map(int, input().split()))

left_socks = {}
right_socks = {}

for i in A[:X]:
    if i not in left_socks:
        left_socks[i] = 1
    else:
        left_socks[i] += 1

for i in A[X:]:
    if i not in right_socks:
        right_socks[i] = 1
    else:
        right_socks[i] += 1

count = 0
for i in left_socks:
    for j in right_socks:
        if i == j: continue
        count += left_socks[i] * right_socks[j]

print(count)