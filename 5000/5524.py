N = int(input())
names = [input().lower() for _ in range(N)]
print(*names, sep="\n")