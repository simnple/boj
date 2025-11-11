import sys

input = sys.stdin.readline

N, K = map(int, input().split())
teams = sorted([input().rstrip().split() for _ in range(N)], key=lambda x: (-int(x[2]), int(x[3])))

univs = []

i = 0
while len(univs) < K:
    if teams[i][0] not in univs:
        univs.append(teams[i][0])
        print(teams[i][1])
    i += 1