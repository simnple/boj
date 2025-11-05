import sys

input = sys.stdin.readline

stack = []

N, M = map(int, input().split())
graph = [set() for _ in range(N + 1)]

know_real_ppl = list(map(int, input().split()))

if know_real_ppl[0]:
    stack = know_real_ppl[1:]

parties = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    if parties[i][0]:
        for j in range(1, parties[i][0] + 1):
            for k in range(1, parties[i][0] + 1):
                graph[parties[i][j]].add(parties[i][k])

visited = [False] * (N + 1)

while stack:
    ppl = stack.pop()

    if not visited[ppl]:
        visited[ppl] = True

        for node_ppl in graph[ppl]:
            if visited[node_ppl]: continue
            elif node_ppl == ppl: continue

            stack.append(node_ppl)

lie_count = 0
for i in range(M):
    if parties[i][0]:
        for j in range(1, parties[i][0] + 1):
            if visited[parties[i][j]]:
                break
        else:
            lie_count += 1

print(lie_count)