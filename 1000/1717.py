import sys

def find_parent(a):
    i = a
    j = groups[i]
    while i != j:
        i = j
        j = groups[i]
    return i

input = sys.stdin.readline

n, m = map(int, input().split())

groups = [i for i in range(n+1)]

for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        if a == b: continue
        a, b = sorted([find_parent(a), find_parent(b)])
        groups[a] = b

    elif k == 1:
        print("YES" if find_parent(a) == find_parent(b) else "NO")