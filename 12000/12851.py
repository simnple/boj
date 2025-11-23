from collections import deque

N, K = map(int, input().split())

visited = [-1] * (100_000 + 1)

queue = deque([N])
result = [N]

while queue and visited[K] == -1:
    node = queue.popleft()

    for x in [node + 1, node - 1, node * 2]:
        if not 0 <= x <= 100_000: continue
        elif visited[x] != -1: continue
        elif x == N: continue

        visited[x] = node
        queue.append(x)

        if x == K:
            current_num = x
            result = [current_num]
            while current_num != N:
                result.append(visited[current_num])
                current_num = visited[current_num]
            break

print(len(result) - 1)
print(*result[::-1])