from collections import deque

SIZE = 9999

primes = [1] * (SIZE + 1)

for i in range(2, int(SIZE ** 0.5) + 1):
    if not primes[i]: continue

    for j in range(i * i, SIZE + 1, i):
        primes[j] = 0

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    queue = deque([n])
    visited = [-1] * (SIZE + 1)
    visited[n] = 0

    while queue:
        node = queue.popleft()

        if node == m:
            print(visited[m])
            break

        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0: continue

                value = list(str(node))
                value[i] = str(j)
                value = int("".join(value))

                if visited[value] > -1: continue
                if not primes[value]: continue

                visited[value] = visited[node] + 1

                queue.append(value)
    else:
        print("Impossible")