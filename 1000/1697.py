from collections import deque

N, K = map(int, input().split())

stack = deque([(N, 0)])
visited = [False] * 100_001

while stack:
    node, move_count = stack.popleft()

    if node == K:
        print(move_count)
        break

    if not 0 <= node <= 100_000: continue
    if visited[node]: continue

    visited[node] = True

    stack.append((node - 1, move_count + 1))
    stack.append((node + 1, move_count + 1))
    stack.append((node * 2, move_count + 1))
