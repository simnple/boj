def n_queen(queens):
    size = len(queens)
    if size == N:
        return 1
    
    x_list = [True] * N

    for y in range(size):
        x = queens[y]

        x_list[x] = False
        diff = abs(y - size)

        if 0 <= x + diff < N:
            x_list[x + diff] = False
        if 0 <= x - diff < N:
            x_list[x - diff] = False

    result = 0
    for x in range(N):
        if not x_list[x]: continue

        result += n_queen(queens + [x])

    return result

N = int(input())

print(n_queen([]))