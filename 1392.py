N, Q = map(int, input().split())

d = [int(input()) for i in range(N)]
_ = [int(input()) for i in range(Q)]
sec = []

for i in range(len(d)):
    for j in range(d[i]):
        sec.append(i+1)

for i in _:
    print(sec[i])