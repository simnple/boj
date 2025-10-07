import sys

_ = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(int(sys.stdin.readline()))]

result = []

for pos in _:
    result.append([pos[1], pos[0]])

for pos in list(sorted(result)):
    print(pos[1], pos[0])