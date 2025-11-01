def matrix_mul(a, b):
    result = [[0] * len(a) for _ in range(len(b[0]))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            total = 0

            for k in range(len(a)):
                total += a[i][k] * b[k][j] % 1000

            result[i][j] = total % 1000

    return result

def matrix_pow(a, b):
    if b == 1:
        result = [[0] * len(a) for _ in range(len(a))]

        for i in range(len(a)):
            for j in range(len(a)):
                result[i][j] = a[i][j] % 1000

        return result

    if b % 2 == 0:
        half = matrix_pow(A, b // 2)
        return matrix_mul(half, half)
    else:
        return matrix_mul(A, matrix_pow(A, b-1))

N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

matrix = matrix_pow(A, B)
for i in range(N):
    print(*matrix[i])