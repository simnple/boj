from collections import deque

N, K = map(int, input().split())

visited = [0] * (100_000 + 1)
counts = [0] * (100_000 + 1)
counts[N] = 1

queue = deque([N])

while queue:
    x = queue.popleft()

    for nx in [x - 1, x + 1, x * 2]:
        if not 0 <= nx < 100_000 + 1: continue
        if nx == N: continue

        if not visited[nx]:
            visited[nx] = visited[x] + 1
            counts[nx] += counts[x]
            queue.append(nx)

        elif visited[nx] == visited[x] + 1:
            counts[nx] += counts[x]

print(visited[K])
print(counts[K])