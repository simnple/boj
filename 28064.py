import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

names = [input() for _ in range(N)]

count = 0
for i in range(len(names)):
    for k in range(i+1, len(names)):
        minimum = min(len(names[i]), len(names[k]))
        for j in range(1, minimum+1):
            if names[i][-j:] == names[k][:j] or names[i][:j] == names[k][-j:]:
                count += 1
                break

print(count)