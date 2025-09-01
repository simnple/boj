N = int(input())

original = [list(map(int, input().split())) for _ in range(N)]

def paper(square, n):
    scale = n ** 2
    colored_box = 0
    uncolored_box = 0

    if scale == sum([sum(box) for box in square]):
        return 0, 1
    elif sum([sum(box) for box in square]) == 0:
        return 1, 0
    else:
        for i in range(2):
            for j in range(0, n, n//2):
                temp_square = []
                for y in range(j, j + n//2):
                    temp_square.append(square[y][(n // 2) * i:(n // 2) * (i + 1)])
                result = paper(temp_square, n//2)

                colored_box += result[1]
                uncolored_box += result[0]

        return uncolored_box, colored_box

print(*paper(original, N), sep="\n")