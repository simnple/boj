graph = [
    [1, 2, 3, 4],
    [0, 2, 3, 5],
    [0, 1, 4, 5],
    [0, 1, 4, 5],
    [0, 2, 3, 5],
    [1, 2, 3, 4]
]

def get_two_surface():
    result = []

    for i in range(6):
        for j in graph[i]:
            result.append(dice[i] + dice[j])

    return min(result)

def get_three_surface():
    result = []

    for i in range(6):
        for j in graph[i]:
            for k in set(graph[i]) & set(graph[j]) - set([i, j]):
                result.append(dice[i] + dice[j] + dice[k])

    return min(result)

N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice) - max(dice))

elif N > 1:
    one_surface = min(dice)
    two_surface = get_two_surface()
    three_surface = get_three_surface()

    print((N - 2) * (N - 1) * one_surface * 4 \
        + (N - 2) * (N - 2) * one_surface \
        + two_surface * 4 * (N - 1) \
        + two_surface * 4 * (N - 2) \
        + three_surface * 4
        )