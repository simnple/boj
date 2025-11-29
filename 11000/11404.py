import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

graphs = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graphs[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())

    if not graphs[a][b]:
        graphs[a][b] = c
    else:
        graphs[a][b] = min(graphs[a][b], c)

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            graphs[start][end] = min(graphs[start][end], graphs[start][mid] + graphs[mid][end])

for start in range(1, n + 1):
    print(*[0 if i == INF else i for i in graphs[start][1:]])
