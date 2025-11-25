import sys

input = sys.stdin.readline

N, K = map(int, input().split())
M = int(input())
S = list(map(int, input().split()))

for i in range(M - 1):
    diff = abs(S[i] - S[i + 1])
    if diff > 1 and diff <= K + 1:
        print("NO")
        break
else:
    if S[-1] == N or N - K - 1 >= S[-1]:
        print("YES")
    else:
        print("NO")