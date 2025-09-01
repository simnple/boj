import sys

def input(): return sys.stdin.readline().rstrip()

data = {}

def get_humans(floor, room):
    if floor == 0:
        return room
    
    else:
        if data.get(f"{floor}-{room}") == None:
            data[f"{floor}-{room}"] = sum([get_humans(floor - 1, i) for i in range(1, room + 1)])
            return data[f"{floor}-{room}"]

        else:
            return data[f"{floor}-{room}"]

_ = [[int(input()) for j in range(2)] for i in range(int(input()))]

for k, n in _:
    print(get_humans(k, n))