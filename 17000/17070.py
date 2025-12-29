import sys

input = sys.stdin.readline
can_moves = [(0, 2), (1, 2), (0, 1, 2)]
diffs = [[(1, 0)], [(0, 1)], [(1, 0), (1, 1), (0, 1)]]
arrival = [(1, 0), (0, 1), (1, 1)]

history = {}

def dfs(x, y, movement):
    if x == y == N - 1:
        return 1

    if (x, y, movement) in history:
        return history[(x, y, movement)]

    else:
        history[(x, y, movement)] = 0

        for i in can_moves[movement]:
            for dx, dy in diffs[i]:
                node_x = x + dx
                node_y = y + dy
                if not (0 <= node_x < N and 0 <= node_y < N): break
                if graph[node_y][node_x]: break

            else:
                next_x = x + arrival[i][0]
                next_y = y + arrival[i][1]
                history[(x, y, movement)] += dfs(next_x, next_y, i)

        return history[(x, y, movement)]

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
graph[0][0] = graph[0][1] = 1

print(dfs(1, 0, 0))