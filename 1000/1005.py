from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))

    in_degree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    for _ in range(K):
        X, Y = map(int, input().split())
        in_degree[Y] += 1
        graph[X].append(Y)

    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    result = D[:]
    while queue:
        node = queue.popleft()

        for i in graph[node]:
            in_degree[i] -= 1
            result[i] = max(result[i], result[node] + D[i])

            if in_degree[i] == 0:
                queue.append(i)

    W = int(input())
    print(result[W])