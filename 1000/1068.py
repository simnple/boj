import sys

input = sys.stdin.readline

N = int(input())
nodes = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for i in range(N):
    if nodes[i] != -1:
        graph[nodes[i]].append(i)

remove_node = int(input())
graph[remove_node] = []

for i in range(N):
    temp = []
    for j in range(len(graph[i])):
        if graph[i][j] != remove_node:
            temp.append(graph[i][j])
    graph[i] = temp

parent = 0
while nodes[parent] != -1:
    parent = nodes[parent]
stack = [parent]

count = 0
while stack:
    node = stack.pop()

    if node != remove_node:
        if not graph[node]:
            count += 1

        for i in range(len(graph[node])):
            stack.append(graph[node][i])

print(count)