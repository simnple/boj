import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

nums = []
for i in range(N):
    nums.append(list(map(int, input().split())))

sum_nums = [[] for i in range(N)]

for y in range(N):
    for x in range(N):
        if x == 0 and y == 0:
            sum_nums[y].append(nums[0][0])
        
        elif x == 0:
            sum_nums[y].append(sum_nums[y-1][N-1] + nums[y][x])
        
        else:
            sum_nums[y].append(sum_nums[y][x-1] + nums[y][x])

# for i in sum_nums:
#     print(i)

for i in range(M):
    cal = lambda x: int(x)-1
    y1, x1, y2, x2 = map(cal, input().split())

    if x1 == y1 == 0:
        if x2 == N-1 or y1 == y2:
            print(sum_nums[y2][x2])
        else:
            result = 0
            for j in range(y2, 0, -1):
                result += sum_nums[j][x2] - sum_nums[j-1][N-1]
            print(result + sum_nums[y1][x2])
    elif x1 == x2 and y1 == y2:
        if x2 == 0:
            print(sum_nums[y2][x2] - sum_nums[y2-1][N-1])
        else:
            print(sum_nums[y2][x2] - sum_nums[y2][x2-1])
    else:
        if x1 > 0:
            result = 0
            for j in range(y2, y1-1, -1):
                result += sum_nums[j][x2] - sum_nums[j][x1-1]
            print(result)
        else:
            result = 0
            for j in range(y2, y1-1, -1):
                result += sum_nums[j][x2] - sum_nums[j-1][N-1]
            print(result)
