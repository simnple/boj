import sys

_ = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(int(sys.stdin.readline()))]

result = []

for pos in _:
    result.append([pos[0], pos[1]])

for pos in list(sorted(result)):
    print(pos[0], pos[1])