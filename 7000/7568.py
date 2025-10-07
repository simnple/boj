N = int(input())
_ = [list(map(int, input().split())) for i in range(N)]

nums = [1] * N

for i in range(0, N):
    for j in range(0, N):
        if _[i][0] < _[j][0] and _[i][1] < _[j][1]:
            nums[i] += 1

print(" ".join(list(map(str, nums))))