import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
trees = list(map(int, input().split()))

minimum = 0
maximum = max(trees)
tree = 0
result = 0

while minimum <= maximum:
    tree = 0
    mid = (maximum + minimum) // 2

    for i in trees:
        if i > mid:
            tree += i - mid
    
    if tree >= M:
        minimum = mid + 1
        result = mid
    
    elif tree < M:
        maximum = mid - 1

print(result)