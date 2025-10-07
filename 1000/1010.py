import math

__ = [list(map(int, input().split())) for i in range(int(input()))]

for _ in __:
    if _[0] < _[1]:
        _.reverse()

    print(math.comb(_[0], _[1]))