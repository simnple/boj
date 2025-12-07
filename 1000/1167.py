import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))[:-1]

    node = data[0]

    for i in range(1, len(data), 2):
        graph[node].append((data[i], data[i + 1]))

diameters = [0] * (V + 1)
visited = [0] * (V + 1)
result = 0

def dfs(start):
    global result

    visited[start] = 1

    temp_diameters = []
    for ne, nw in graph[start]:
        if not visited[ne]:
            temp_diameters.append(dfs(ne) + nw)

    temp_diameters.sort()
    if temp_diameters:
        diameters[start] = temp_diameters[-1]
        result = max(result, temp_diameters[-1])

    if len(temp_diameters) > 1:
        result = max(result, temp_diameters[-1] + temp_diameters[-2])

    return diameters[start]

dfs(1)
print(result)