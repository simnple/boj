import sys

input = sys.stdin.readline

n = int(input())
visited = [0] * (n + 1)
visited[1] = 1

m = int(input())

friends = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

result = 0

for i in friends[1]:
    if not visited[i]: result += 1

    visited[i] = 1
    for j in friends[i]:
        if not visited[j]:
            visited[j] = 1
            result += 1

print(result)