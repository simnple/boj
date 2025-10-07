N = int(input())
datas = dict()

for _ in range(N):
    d = input().split()
    datas[d[0]] = list(map(int, d[1:]))

print(max(datas, key=lambda x: (datas[x][2], datas[x][1], datas[x][0])))
print(max(datas, key=lambda x: (-datas[x][2], -datas[x][1], -datas[x][0])))
