data = {}

def cal(idx):
    if data.get(idx-1) == None:
        data[idx-1] = (cal(idx-1) if idx-1 > -1 else 0)

    return _[idx] + data[idx-1]

size = int(input())
_ = list(map(int, input().split()))
_.sort()

print(sum([cal(i) for i in range(size)]))