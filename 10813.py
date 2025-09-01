N, M = map(int, input().split())

nums = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    t = nums[i-1]
    nums[i-1] = nums[j-1]
    nums[j-1] = t

print(*nums)