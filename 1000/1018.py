N, M = map(int, input().split())

BOARD_X = 8
BOARD_Y = 8

char = {
    0: {0: "B", 1: "W"},
    1: {0: "W", 1: "B"}
}

chk = [[], []]

for _ in range(2):
    for i in range(1, BOARD_X + 1):
        chk[_].append([])
        for j in range(1, BOARD_Y + 1):
            chk[_][i-1].append(char[_][abs(j%2 - i%2)])

board = []
for i in range(N):
    board.append(list(input()))

result = N*M+1
for i in range(N - BOARD_Y + 1):
    for j in range(M - BOARD_X + 1):
        for mode in range(2):
            count = 0
            for y in range(i, i+BOARD_Y):
                for x in range(j, j+BOARD_X):
                    if board[y][x] != chk[mode][y-i][x-j]:
                        count += 1
            if result > count: result = count
            if result == 0: break

print(result)