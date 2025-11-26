N = int(input())

visited = [0] * N
visited_diag1 = [0] * (N * 2)
visited_diag2 = [0] * (N * 2)
result = []
count = 0

def dfs():
    global count
    if len(result) == N:
        count += 1
        return

    y = len(result)
    for x in range(N):
        if visited[x]: continue
        if visited_diag1[x + y]: continue
        if visited_diag2[N + x - y]: continue

        visited[x] = 1
        visited_diag1[x + y] = 1
        visited_diag2[N + x - y] = 1
        result.append(x)

        dfs()

        visited[x] = 0
        visited_diag1[x + y] = 0
        visited_diag2[N + x - y] = 0
        result.pop()

dfs()
print(count)