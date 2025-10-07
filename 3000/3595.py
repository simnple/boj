n = int(input())

nums = []
for i in range(1, n+1):
    if n % i == 0:
        nums.append(i)

minimum = n ** 4
patterns = [n, n, n]
for i in nums:
    for j in nums:
        if i * j > n: break
        for k in nums:
            t = i * j * k
            scale = 2 * (i*j + j*k + k*i)
            if t > n: break
            elif t == n and scale < minimum:
                minimum = scale
                patterns = [i, j, k]

print(*patterns)
