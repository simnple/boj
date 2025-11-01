def lmsr(s):
    l = len(s)
    s += s

    i = j = k = 0
    j = 1

    while i < l and j < l and k < l:
        if s[i+k] > s[j+k]:
            i += k + 1
            j = i + 1
            k = 0
        elif s[i+k] < s[j+k]:
            j += k + 1
            k = 0
        else:
            k += 1
    return i + 1

import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    print(lmsr(input().rstrip()))