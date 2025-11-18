import sys

input = sys.stdin.readline
diffs = [(-2, 0), (2, 0), (0, 2), (0, -2)]

N, K = map(int, input().split())
box = set()

stack = []
for _ in range(K):
    X, Y = map(int, input().split())
    box.add((X, Y))
    stack.append((X, Y))

count = 0
while stack:
    x, y = stack.pop()

    for dx, dy in diffs:
        if not (1 <= x + dx < N + 1 and 1 <= y + dy < N + 1): continue
        if (x + dx, y + dy) in box: continue

        box.add((x + dx, y + dy))
        count += 1

print(count)