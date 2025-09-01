N = int(input())
X = list(map(int, input().split()))

nums = [0] * (N + 1)

for i in range(len(X)):
    # i + 1

    idx = X[i]
    if nums[idx] == 0:
        