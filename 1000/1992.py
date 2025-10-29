import sys

input = sys.stdin.readline

def decompress(x, y, size):
    for i in range(y, y+size):
        for j in range(x, x+size):
            if data[y][x] != data[i][j]:
                size //= 2
                result = "("
                result += decompress(x, y, size)
                result += decompress(x + size, y, size)
                result += decompress(x, y + size, size)
                result += decompress(x + size, y + size, size)
                result += ")"
                return result
    else:
        return data[y][x]

N = int(input())
data = [list(input().rstrip()) for _ in range(N)]

print(decompress(0, 0, N))