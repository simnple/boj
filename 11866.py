import sys

N, K = map(int, sys.stdin.readline().split())

_ = [i for i in range(1,N+1)]

result = []

count = 1
while len(_) > 0:
    if count == K:
        result.append(_[0])
        del(_[0])
        count = 0

    else:
        _.append(_[0])
        del(_[0])

    count += 1

print(f"<{', '.join(list(map(str, result)))}>")