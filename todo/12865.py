import sys

input = sys.stdin.readline

N, K = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]
items = sorted(items, key=lambda x: x[0])
dp = [[0, 0] for _ in range(N)]

"""
5 7
1 6
6 13
4 8
3 2
5 12
"""

print(items)
for i in range(N):
    W1, V1 = items[i]

    for j in range(i):
        W2, V2 = items[j]

        # 1 -> 대장
        # 2 -> 부하

        # 만약 