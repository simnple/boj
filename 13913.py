from collections import deque

N, K = map(int, input().split())

stack = deque([(N, 0, [N])])
visited = [False] * 100_001

while stack:
    node, move_count, move_pattern = stack.popleft()

    if node == K:
        print(move_count)
        print(*move_pattern)
        break

    if K + 1 < node: continue
    if not 0 <= node <= 100_000: continue
    if visited[node]: continue

    print(stack)

    stack.append((node - 1, move_count + 1, move_pattern + [node - 1]))
    stack.append((node + 1, move_count + 1, move_pattern + [node + 1]))
    stack.append((node * 2, move_count + 1, move_pattern + [node * 2]))
