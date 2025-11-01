import sys

def get_cycle_position(s):
    l = len(s)
    s += s

    i = 0
    j = 1
    k = 0
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

    return i

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    L, S = input().rstrip().split()
    print(get_cycle_position(S))