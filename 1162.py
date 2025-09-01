import sys

N, M, K = map(int, sys.stdin.readline().split())
_ = [sys.stdin.readline().split() for i in range(N)]

data = {}

for dummy in _:
    data[f"{dummy[0]}-{dummy[1]}"] = int(dummy[2])

for road in data:
    if road[0] == "1":
        print(road)