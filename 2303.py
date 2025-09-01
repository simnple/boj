import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
result = [0] * N

for i in range(N):
    for j in range(5):
        for k in range(j + 1, 5):
            for l in range(k + 1, 5):
                if result[i] < (nums[i][j]+nums[i][k]+nums[i][l]) % 10:
                    result[i] = (nums[i][j]+nums[i][k]+nums[i][l]) % 10

winner = [0, 0]
for i in range(N):
    if winner[1] <= result[i]:
        winner = [i+1, result[i]]

print(winner[0])