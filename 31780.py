import math

X, M = map(int, input().split())

total = X
childs = [X]
for _ in range(M):
    temp_childs = []
    for i in childs:
        if i == 0: continue

        total += int(i/2)
        total += math.ceil(i/2)

        temp_childs.append(int(i/2))
        temp_childs.append(math.ceil(i/2))

    childs = temp_childs

print(total)