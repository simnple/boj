def calculate_empty(n):
    return [[" " * n] for _ in range(n)]

def calculate_star(n):
    if n == 3:
        return [
            ["***"],
            ["* *"],
            ["***"]
        ]

    else:
        calculated_star = calculate_star(n // 3)
        box = [
            [calculated_star, calculated_star, calculated_star],
            [calculated_star, calculate_empty(n // 3), calculated_star],
            [calculated_star, calculated_star, calculated_star]
        ]
        result = [[] for _ in range(n)]

        for y in range(3):
            for e in range(n // 3):
                line = []
                for x in range(3):
                    line.append(box[y][x][e][0])
                result[y * (n // 3) + e].append("".join(line))

        return result

n = int(input())
for s in calculate_star(n):
    print(s[0])