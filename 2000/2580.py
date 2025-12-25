import sys

nums = [[] for _ in range(9)]
for i in range(9):
    nums[i] = list(map(int, input().split()))

row_visited = [[0] * 10 for _ in range(9)]
col_visited = [[0] * 10 for _ in range(9)]
visited = [[[0] * 10 for _ in range(3)] for _ in range(3)]

for i in range(9):
    for j in range(9):
        if nums[i][j] == 0: continue
        row_visited[i][nums[i][j]] = 1

for i in range(9):
    for j in range(9):
        if nums[j][i] == 0: continue
        col_visited[i][nums[j][i]] = 1

for i in range(9):
    for j in range(9):
        if nums[i][j] == 0: continue
        visited[i // 3][j // 3][nums[i][j]] = 1

curr_row = 0
curr_col = 0

def backtracking():
    global curr_row, curr_col
    if curr_row == 9 and curr_col == 0:
        for i in range(9):
            print(" ".join(map(str, nums[i])))
        sys.exit()
    
    else:
        if nums[curr_row][curr_col]:
            curr_col += 1
            if curr_col > 8:
                curr_col = 0
                curr_row += 1
            backtracking()

        else:
            last_row = curr_row
            last_col = curr_col

            for n in range(1, 10):
                if row_visited[last_row][n]: continue
                elif col_visited[last_col][n]: continue
                elif visited[last_row // 3][last_col // 3][n]: continue

                row_visited[last_row][n] = 1
                col_visited[last_col][n] = 1
                visited[last_row // 3][last_col // 3][n] = 1
                nums[last_row][last_col] = n
                
                curr_col += 1
                if curr_col > 8:
                    curr_col = 0
                    curr_row += 1

                backtracking()

                row_visited[last_row][n] = 0
                col_visited[last_col][n] = 0
                visited[last_row // 3][last_col // 3][n] = 0
                nums[last_row][last_col] = 0

                curr_col = last_col
                curr_row = last_row

backtracking()