import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = int(input())

ppl = [0] * (N + 1)
time_table = [[] for _ in range(M + S)]
count = 0

result = []
for j in range(M):
    i, t = map(int, input().split())
    if t == 0:
        ppl[i] += 1
        count += 1

        for k in time_table[count]:
            if ppl[k] == 2:
                result.append(k)

    elif t == 1:
        ppl[i] += 2
        if ppl[i] == 2:
            time_table[count + S].append(i)

if not result:
    print(-1)
else:
    print(*sorted(result), sep="\n")