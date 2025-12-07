N = int(input())

graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
out_degree = [0] * (N + 1)

for _ in range(N - 1):
    parent, child, weight = map(int, input().split())

    graph[parent].append((child, weight))
    out_degree[parent] += 1
    in_degree[child] += 1

result = 0
for i in range(1, N + 1):
    total = []
    if out_degree[i] < 2 and in_degree[i] > 0 and i != 1:
        continue

    for child, weight in graph[i]:
        stack = [(child, weight)]

        max_distance = 0

        while stack:
            node_child, node_weight = stack.pop()

            max_distance = max(max_distance, node_weight)

            for nc, nw in graph[node_child]:
                max_distance = max(max_distance, nw + node_weight)
                stack.append((nc, nw + node_weight))

        total.append(max_distance)

    if len(total) > 1:
        result = max(result, sum(sorted(total)[-2:]))
    elif total:
        result = max(result, total[0])

print(result)