box = [input().split() for _ in range(10)]

def can_durem():
    for i in range(10):
        prev_row = box[i][0]

        for j in range(10):
            if prev_row != box[i][j]:
                break

            elif j == 9:
                return 1

            prev_row = box[i][j]

    for i in range(10):
        prev_col = box[0][i]

        for j in range(10):
            if prev_col != box[j][i]:
                break

            elif j == 9:
                return 1

            prev_col = box[j][i]

    return 0

print(can_durem())