import sys

N = int(input())

words = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if words[i][j] != words[j][i]:
            print("NO")
            sys.exit()

print("YES")