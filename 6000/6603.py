def dfs():
    if len(result) == 6:
        print(" ".join(map(lambda x: str(S[x]), result)))
        return
    
    last_result = 0
    if result:
        last_result = result[-1]

    for i in range(last_result, k):
        if visited[i]: continue

        visited[i] = 1
        result.append(i)

        dfs()

        result.pop()
        visited[i] = 0

while True:
    data = list(map(int, input().split()))
    if data[0] == 0: break

    k, S = data[0], data[1:]

    visited = [0] * k
    result = []

    dfs()

    print()