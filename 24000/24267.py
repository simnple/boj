n = int(input())
print(sum([i * (n-1-i) for i in range(1, n-1)]), 3, sep="\n")