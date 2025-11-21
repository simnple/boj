from collections import deque

N, K = map(int, input().split())

visited = [0] * (100_000 + 1)

queue = deque([N])

while queue:
    node = queue.popleft()

    for x in [node - 1, node + 1, node * 2]:
        if not (0 <= x <= 100_000): continue
        if visited[x]: continue
        if x == N: continue

        visited[x] = visited[node] + 1
        queue.append(x)

print(visited[K])