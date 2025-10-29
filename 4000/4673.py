def d(n):
    return n + sum(map(int, str(n)))

creator_nums = [0] * 10001

for i in range(1, 10001):
    if creator_nums[i]: continue

    n = d(i)
    while n <= 10000:
        if creator_nums[n]: break
        creator_nums[n] = d(n)
        n = creator_nums[n]

for i in range(1, 10000):
    if not creator_nums[i]:
        print(i)