from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
tower = list(map(int, input().split()))
temp = []
result = [0] * N

for i in range(N):
    while temp and temp[-1][1] < tower[i]:
        temp.pop()

    if temp:
        result[i] = temp[-1][0]

    temp.append((i + 1, tower[i]))

print(*result)